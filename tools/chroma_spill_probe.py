from PIL import Image
import numpy as np, math, random
random.seed(11)
W,H=1500,750; KEY=np.array([0,255,0])

# subject with hairy edge, rendered ANTI-ALIASED against the green field
# => edge pixels are genuine blends of subject+green: that IS the spill
img=Image.new("RGB",(W,H),tuple(KEY)); px=img.load()
cx,cy=W//2,H//2; brx,bry=380,210
sub=np.array([120,98,74])
for y in range(H):
    for x in range(W):
        d=((x-cx)/brx)**2+((y-cy)/bry)**2
        if d<=1.0: px[x,y]=tuple(sub)
        elif d<=1.06:                       # soft antialiased rim
            t=(d-1.0)/0.06
            px[x,y]=tuple((sub*(1-t)+KEY*t).astype(int))
for i in range(3000):
    a=random.uniform(0,2*math.pi); L=random.uniform(25,100)
    sx=cx+brx*math.cos(a); sy=cy+bry*math.sin(a)
    for t in range(int(L)):
        f=t/L
        x=int(sx+math.cos(a)*t); y=int(sy+math.sin(a)*t)
        if 0<=x<W and 0<=y<H:
            px[x,y]=tuple((sub*(1-f*0.8)+KEY*(f*0.8)).astype(int))  # bristle fades into green

arr=np.asarray(img).astype(np.float64)
# alpha from greenness: fully green -> 0, no green -> 255
gness=np.clip((arr[:,:,1]-(arr[:,:,0]+arr[:,:,2])/2)/255.0,0,1)
alpha=((1-gness)*255).astype(np.uint8)

def despill(rgb):
    r,g,b=rgb[:,:,0],rgb[:,:,1],rgb[:,:,2]
    cap=np.maximum(r,b)
    return np.dstack([r,np.minimum(g,cap),b])

for label,rgb in (("keyed only",arr.copy()),("keyed + despilled",despill(arr.copy()))):
    im=Image.fromarray(np.dstack([rgb,alpha]).astype(np.uint8),"RGBA")
    print(f"\n{label}")
    print(f"  {'scale':18s} {'semi-α px':>10s} {'mean G-excess':>14s} {'px G-excess>15':>15s}")
    for stage,size in (("source 1500x750",(W,H)),("runtime 384x181",(384,181)),("gameplay 96x46",(96,46))):
        s=im if size==(W,H) else im.resize(size,Image.LANCZOS)
        a=np.asarray(s).astype(np.int16)
        semi=(a[:,:,3]>8)&(a[:,:,3]<248)
        if semi.sum()==0: print(f"  {stage:18s} {0:10d} {'-':>14s} {'-':>15s}"); continue
        gx=(a[:,:,1]-np.maximum(a[:,:,0],a[:,:,2]))[semi]
        print(f"  {stage:18s} {int(semi.sum()):10d} {gx.mean():14.2f} {int((gx>15).sum()):15d}")
