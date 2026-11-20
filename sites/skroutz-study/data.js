/* Mock catalogue for the layout study. Everything here is invented. */
window.KDATA = (function () {
  const categories = [
    { slug: 'tech', name: 'Τεχνολογία', icon: '💻', subs: [
      ['Κινητά Τηλέφωνα', ['Smartphones', 'Θήκες Κινητών', 'Φορτιστές', 'Power Banks']],
      ['Υπολογιστές', ['Laptops', 'Desktop', 'Οθόνες', 'Πληκτρολόγια', 'Ποντίκια']],
      ['Ήχος', ['Ακουστικά', 'Ηχεία Bluetooth', 'Soundbars']],
      ['Εικόνα', ['Τηλεοράσεις', 'Projectors', 'Streaming Devices']],
      ['Gaming', ['Κονσόλες', 'Παιχνίδια', 'Χειριστήρια']],
      ['Smartwatches', ['Smartwatches', 'Activity Trackers']] ] },
    { slug: 'home', name: 'Σπίτι - Κήπος', icon: '🏠', subs: [
      ['Οικιακές Συσκευές', ['Ψυγεία', 'Πλυντήρια', 'Σκούπες', 'Καφετιέρες']],
      ['Έπιπλα', ['Καναπέδες', 'Καρέκλες', 'Γραφεία', 'Κρεβάτια']],
      ['Κουζίνα', ['Μαγειρικά Σκεύη', 'Μαχαίρια', 'Air Fryers']],
      ['Κήπος', ['Εργαλεία Κήπου', 'Ψησταριές', 'Έπιπλα Κήπου']] ] },
    { slug: 'fashion', name: 'Μόδα', icon: '👟', subs: [
      ['Γυναικεία', ['Φορέματα', 'Τσάντες', 'Παπούτσια']],
      ['Ανδρικά', ['T-shirts', 'Τζιν', 'Sneakers']],
      ['Αξεσουάρ', ['Ρολόγια', 'Γυαλιά Ηλίου', 'Πορτοφόλια']] ] },
    { slug: 'beauty', name: 'Υγεία - Ομορφιά', icon: '💄', subs: [
      ['Περιποίηση Προσώπου', ['Κρέμες', 'Serum', 'Αντηλιακά']],
      ['Αρώματα', ['Γυναικεία', 'Ανδρικά']],
      ['Συμπληρώματα', ['Βιταμίνες', 'Πρωτεΐνες']] ] },
    { slug: 'kids', name: 'Παιδικά - Βρεφικά', icon: '🧸', subs: [
      ['Παιχνίδια', ['LEGO', 'Επιτραπέζια', 'Κούκλες']],
      ['Βρεφικά', ['Καρότσια', 'Πάνες', 'Καθισματάκια']] ] },
    { slug: 'sports', name: 'Hobby - Αθλητισμός', icon: '🚲', subs: [
      ['Fitness', ['Αλτήρες', 'Διάδρομοι', 'Yoga']],
      ['Ποδήλατα', ['Ποδήλατα Βουνού', 'Ηλεκτρικά Ποδήλατα', 'Πατίνια']],
      ['Βιβλία', ['Λογοτεχνία', 'Παιδικά Βιβλία']] ] },
    { slug: 'auto', name: 'Μηχανοκίνηση', icon: '🚗', subs: [
      ['Αυτοκίνητο', ['Ελαστικά', 'Λάδια', 'Dash Cams']],
      ['Μοτοσυκλέτα', ['Κράνη', 'Μπουφάν']] ] },
    { slug: 'pets', name: 'Κατοικίδια', icon: '🐶', subs: [
      ['Σκύλοι', ['Τροφές', 'Λουριά', 'Κρεβάτια']],
      ['Γάτες', ['Τροφές', 'Άμμος', 'Ονυχοδρόμια']] ] },
    { slug: 'office', name: 'Επαγγελματικά', icon: '🧰', subs: [
      ['Εργαλεία', ['Δράπανα', 'Κατσαβίδια', 'Σετ Εργαλείων']],
      ['Γραφείο', ['Εκτυπωτές', 'Χαρτικά']] ] }
  ];

  // [name, category, icon, base price, rating, reviews, subcategory, hue]
  const seed = [
    ['Nova X14 Pro 256GB Μαύρο', 'tech', '📱', 899, 4.6, 1284, 'Smartphones', 220],
    ['Nova X14 128GB Μπλε', 'tech', '📱', 649, 4.5, 932, 'Smartphones', 210],
    ['Pixelon 9a 128GB', 'tech', '📱', 429, 4.4, 611, 'Smartphones', 150],
    ['Aerobook 14 M3 16GB/512GB', 'tech', '💻', 1349, 4.8, 402, 'Laptops', 260],
    ['Vektor Gaming 16 RTX', 'tech', '💻', 1599, 4.3, 188, 'Laptops', 0],
    ['Sonora QC Wireless Ακουστικά', 'tech', '🎧', 279, 4.7, 2210, 'Ακουστικά', 30],
    ['Sonora Buds 3 True Wireless', 'tech', '🎧', 129, 4.4, 1530, 'Ακουστικά', 40],
    ['Boomcube Mini Ηχείο Bluetooth', 'tech', '🔊', 49.9, 4.5, 3021, 'Ηχεία Bluetooth', 190],
    ['Lumina 55" 4K OLED Smart TV', 'tech', '📺', 1149, 4.6, 344, 'Τηλεοράσεις', 240],
    ['PlayBox 5 Slim Digital', 'tech', '🎮', 449, 4.8, 5120, 'Κονσόλες', 230],
    ['Tempo Watch 7 GPS 44mm', 'tech', '⌚', 329, 4.5, 870, 'Smartwatches', 330],
    ['Volt 20000mAh Power Bank', 'tech', '🔋', 24.9, 4.3, 4410, 'Power Banks', 100],
    ['Crema Espresso Μηχανή 15bar', 'home', '☕', 189, 4.6, 1202, 'Καφετιέρες', 25],
    ['Cyclo V12 Σκούπα Stick', 'home', '🧹', 399, 4.7, 760, 'Σκούπες', 280],
    ['Crispo XL Air Fryer 6.5L', 'home', '🍟', 99, 4.5, 6230, 'Air Fryers', 45],
    ['Nordic Καναπές 3θέσιος Γκρι', 'home', '🛋️', 499, 4.2, 98, 'Καναπέδες', 200],
    ['Ergo Καρέκλα Γραφείου Mesh', 'home', '🪑', 159, 4.4, 512, 'Καρέκλες', 170],
    ['Grillmaster Ψησταριά Υγραερίου', 'home', '🔥', 349, 4.3, 143, 'Ψησταριές', 10],
    ['Runline 42 Ανδρικά Sneakers', 'fashion', '👟', 89.9, 4.5, 1980, 'Sneakers', 0],
    ['Classic Denim Τζιν Slim', 'fashion', '👖', 49.9, 4.2, 640, 'Τζιν', 215],
    ['Solare Γυαλιά Ηλίου Polarized', 'fashion', '🕶️', 119, 4.6, 410, 'Γυαλιά Ηλίου', 50],
    ['Hydra Serum Υαλουρονικό 30ml', 'beauty', '🧴', 18.5, 4.7, 3320, 'Serum', 300],
    ['SPF50+ Αντηλιακό Προσώπου', 'beauty', '☀️', 14.9, 4.6, 2780, 'Αντηλιακά', 55],
    ['Noir Eau de Parfum 100ml', 'beauty', '🌸', 79, 4.5, 920, 'Γυναικεία', 320],
    ['Vita D3 2000IU 120 caps', 'beauty', '💊', 9.9, 4.8, 5400, 'Βιταμίνες', 90],
    ['Brick City Σταθμός Πυροσβεστικής', 'kids', '🧱', 69.9, 4.9, 820, 'LEGO', 5],
    ['Κατάκτηση Επιτραπέζιο', 'kids', '🎲', 34.9, 4.6, 410, 'Επιτραπέζια', 120],
    ['Breeze Καρότσι Μωρού 3σε1', 'kids', '👶', 379, 4.4, 230, 'Καρότσια', 180],
    ['Trail 29" Ποδήλατο Βουνού', 'sports', '🚵', 549, 4.5, 156, 'Ποδήλατα Βουνού', 130],
    ['Glide E-Scooter 350W', 'sports', '🛴', 399, 4.3, 980, 'Πατίνια', 160],
    ['Ρυθμιζόμενοι Αλτήρες 2x24kg', 'sports', '🏋️', 229, 4.6, 340, 'Αλτήρες', 15],
    ['Yoga Mat 6mm Αντιολισθητικό', 'sports', '🧘', 22.9, 4.5, 1890, 'Yoga', 280],
    ['AllSeason 205/55 R16 Ελαστικό', 'auto', '🛞', 74, 4.4, 620, 'Ελαστικά', 220],
    ['RoadEye 4K Dash Cam', 'auto', '📷', 89, 4.2, 410, 'Dash Cams', 200],
    ['Shield Κράνος Full Face', 'auto', '⛑️', 159, 4.5, 280, 'Κράνη', 0],
    ['Happy Paws Ξηρά Τροφή 12kg', 'pets', '🦴', 42.9, 4.7, 2150, 'Τροφές', 35],
    ['Cozy Κρεβάτι Σκύλου L', 'pets', '🐕', 39.9, 4.6, 760, 'Κρεβάτια', 25],
    ['Torq 18V Δράπανο Μπαταρίας', 'office', '🔩', 119, 4.6, 1120, 'Δράπανα', 50],
    ['InkJet Pro Πολυμηχάνημα WiFi', 'office', '🖨️', 129, 4.1, 540, 'Εκτυπωτές', 210],
    ['Σετ Εργαλείων 108τμχ', 'office', '🧰', 59.9, 4.5, 870, 'Σετ Εργαλείων', 0]
  ];

  const shopNames = ['TechPoint', 'eShop Αθήνα', 'MegaStore', 'Plaisio-like', 'Netstore', 'Kotsovolos-like',
    'Shopflix-like', 'BestPrice Shop', 'Electro Hub', 'Θεσσαλονίκη Direct', 'Κρήτη Market', 'Smart Deals'];

  // Deterministic PRNG so prices are stable across reloads.
  function rng(seedNum) { let s = seedNum >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }

  const products = seed.map((s, i) => {
    const r = rng(i * 7919 + 17);
    const nShops = 3 + Math.floor(r() * 9);
    const shops = [];
    const used = new Set();
    for (let k = 0; k < nShops; k++) {
      let idx; do { idx = Math.floor(r() * shopNames.length); } while (used.has(idx) && used.size < shopNames.length);
      used.add(idx);
      const price = +(s[3] * (0.9 + r() * 0.28)).toFixed(2);
      shops.push({ name: shopNames[idx], price, rating: +(3.8 + r() * 1.2).toFixed(1),
        shipping: r() > 0.5 ? 0 : +(2.5 + r() * 3).toFixed(2), plus: r() > 0.45, stock: r() > 0.15 ? 'Άμεσα διαθέσιμο' : 'Παράδοση σε 4-10 ημέρες' });
    }
    shops.sort((a, b) => a.price - b.price);
    const discount = r() > 0.55 ? Math.floor(8 + r() * 30) : 0;
    return { id: i + 1, name: s[0], cat: s[1], icon: s[2], sub: s[6], hue: s[7], rating: s[4], reviews: s[5],
      shops, min: shops[0].price, discount, oldPrice: discount ? +(shops[0].price / (1 - discount / 100)).toFixed(2) : 0 };
  });

  const brands = ['Nova', 'Sonora', 'Lumina', 'Aerobook', 'Crispo', 'Cyclo', 'Runline', 'Tempo', 'Torq', 'Glide', 'Hydra', 'Brick City'];

  return { categories, products, brands };
})();
