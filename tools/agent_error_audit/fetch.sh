set -u
REPOS="superbot idea-engine substrate-kit superbot-next Substrate-kit-app websites sim-lab venture-lab gba-homebrew spider-swing superbot-games trading-strategy superbot-idle superbot-mineverse pokemon-mod-lab shiftlife product-forge couch-legend spider-bot creator-kit curious-research estate-backups"
for r in $REPOS; do
  ( curl -sSL --noproxy '*' -H "Authorization: Bearer $GITHUB_PAT" \
      "https://api.github.com/repos/menno420/$r/tarball/main" -o "corpus/$r.tar.gz" 2>"corpus/$r.err"
    code=$?
    if [ $code -ne 0 ]; then echo "$r FETCH_FAIL:$code"; else
      mkdir -p "corpus/$r"
      tar -xzf "corpus/$r.tar.gz" -C "corpus/$r" --strip-components=1 \
        --wildcards '*/.sessions/*' '*/docs/findings/*' '*/docs/retro/*' '*/docs/traps*' \
        '*/docs/reviews/*' '*/docs/audits/*' '*/docs/current-state.md' '*/docs/PROJECT-CLOSEOUT.md' \
        '*/CLAUDE.md' '*/.claude/*' '*/docs/program/*' '*/control/*' 2>/dev/null
      echo "$r OK $(find corpus/$r -name '*.md' 2>/dev/null | wc -l) md files"
      rm -f "corpus/$r.tar.gz"
    fi )
done
