# Recall History — PyWorkout


## Session a5bbc541 — 2026-08-14 15:41

**You:** This folder contains all of my github repos. I want to update my README, license, code of conduct, security.md etc for all the repos, and move to a /docs folder for each repo which houses complete markdown docs, which are pushed to a site via mkdocs and github pages. Create a plan for implemeneting the doc rewrite, later we will create a mkdocs template and plan for the /docs folder and website.

**Claude:** I'll start by exploring the folder structure to understand what I'm working with.
  - `PowerShell: Get-ChildItem -Path "D:\W\willtheorangeguy" -Directory | Select-Object -ExpandProperty Name`

**Claude:** Large scope — 121 directories. Let me survey the current state of community-health files.
  - `PowerShell: $repos = Get-ChildItem -Path "D:\W\willtheorangeguy" -Directory $results = foreach ($r in $repos) { $files = Get-ChildItem -Path $r.FullName -File -ErrorAction`

**Claude:** Now let me examine the `.github` org repo (which provides defaults) and representative exemplars.
  - `PowerShell: Write-Output "=== .github repo tree ===" Get-ChildItem -Path "D:\W\willtheorangeguy\.github" -Recurse -File | Where-Object { $_.FullName -notmatch '\\\.git\\' }`
  - `PowerShell: $base="D:\W\willtheorangeguy\.github" foreach ($f in @("README.md","SECURITY.md","CODE_OF_CONDUCT.md","CONTRIBUTING.md","LICENSE.md")) { Write-Output "===== $f`
  - `PowerShell: $repos = Get-ChildItem -Path "D:\W\willtheorangeguy" -Directory Write-Output "=== LICENSE first-line variety ===" $lic = foreach ($r in $repos) { $f = Get-Child`

**Claude:** Strong existing conventions found. Let me dig into README structure, project types, and CI.
  - `Agent: Explore`
  - `Agent: Explore`

**Claude:** Reconnaissance is complete and gives a clear picture. Key findings before I finalize:

- **~121 repos**, 109 on `main`, 14 on `master`, `notes` on `v4`
- **Zero mkdocs/Sphinx anywhere** — greenfield, but an org-level `.github` repo already supplies COC/CONTRIBUTING/SECURITY/LICENSE defaults to every repo that lacks its own
- **A house style already exists**: 18 "mature" repos share a byte-identical README skeleton (Key Features → Download → How To Use → Support → Contributing → Changelog → Credits → Contributors → You may also like → License) and a `docs/` convention (`README.md`, `USAGE.md`, `CUSTOMIZATION.md`, `TESTING.md`, `images/`, `legal/PRIVACY.md`+`TERMS.md`)
- **Conflicts to route around**: 12 repos publish Pages from repo root, `git-rewrite-commits` publishes from `docs/` with an `index.html`, 3 CPSC repos use Jekyll, 4 use Astro/Quartz, 4 have legacy `gh-pages` branches
- **License chaos**: 28 distinct copyright headers across MIT/GPL-3/CC-BY-4.0/Apache-2.0/BSD-2, including stray holders like "Not A Real Person", "Aiming Lab", "Miguel Piedrafita" — and ~36 repos with no LICENSE at all
- **Scale outliers**: transcript archives hold up to 19,700 markdown files each

Four decisions shape the plan:
  - `AskUserQuestion`

**Claude:** Understood — mkdocs is out of scope; this plan covers the content rewrite and the `/docs` migration only. Let me design the execution mechanics.
  - `Agent: Plan`

**Claude:** Let me verify a few of the agent's key claims before committing them to the plan.
  - `PowerShell: Write-Output "=== dir count (incl hidden) ===" (Get-ChildItem "D:\W\willtheorangeguy" -Directory -Force | Where-Object { Test-Path (Join-Path $_.FullName ".git"`

**Claude:** All claims verified: **125 repos**, **12 READMEs with non-rendering `/blob/` image URLs**, `aibot` on a feature branch, `notes` on `v4`, and a 65/21 `LICENSE.md`/`LICENSE` split. Writing the plan.
  - `Write: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `ToolSearch: select:ExitPlanMode`
  - `ExitPlanMode: # Documentation Standardization Across 125 Repos ## Context `D:\W\willtheorangeguy` holds 125 independent git repos accumulated over roughly a decade. Their doc`

**Claude:** Two changes noted. Let me check what images actually exist so the `.github/icons/` move is concrete.
  - `PowerShell: $base="D:\W\willtheorangeguy" Get-ChildItem $base -Directory -Force | ForEach-Object { $d = Join-Path $_.FullName "docs\images" if (Test-Path $d) { $imgs = Get-`

**Claude:** 47 images across 20 repos (~32 MB, dominated by two GIFs — PyTricks-Archive's is 23.8 MB). Note that **18 of them are named `logo.png`**, so a flat `icons/` folder would collide — I'll use per-repo subfolders. Updating the plan.
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`

**Claude:** Now the README template — removing the two sections:
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Grep: Changelog|You may also like|docs/images|images/|CHANGELOG`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`

**Claude:** Now the wave plan, risks, and verification checks:
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`

**Claude:** Now the risk list — centralizing images resolves one risk and introduces another:
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`

**Claude:** Finally, updating the Context section so the goal reflects both changes:
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`

**Claude:** Plan updated with both changes.

**Changelog / You may also like** — struck from the README template, the mandatory/conditional list, the nav block, and added as verification check #12 so the 18 mature repos that carry them today get caught. `CHANGELOG.md` files stay on disk, just unlinked. Removing "You may also like..." also retires the cross-repo deep-link breakage that was risk #13.

**`.github/icons/`** — all 47 images move there, referenced as `raw.githubusercontent.com/willtheorangeguy/.github/main/icons/{REPO}/{FILE}`. Built into Wave 0, with a new Wave 0.6 that curl-sweeps every icon URL before any repo points at it.

Three things about the icons move you should know before approving:

- **18 images are named `logo.png`**, so a flat folder can't hold them — the plan uses per-repo subfolders.
- **This makes `.github` a single point of failure for every image in all 125 repos.** Renaming it or making it private breaks everything at once, silently. That's now risk #3, with branch protection as the mitigation. The upside is real though: since every image URL now sits on `.github`'s `main`, the branch-drift hazard for the 14 `master` repos and `notes` on `v4` disappears entirely.
- **Deleting `docs/images/` reclaims no space** — ~32 MB of blobs stay in those 20 repos' histories. Only a rewrite removes them, which I've flagged as a separate decision rather than folding in.

I also flagged `PyTricks-Archive/welcome.gif` (23.8 MB) and `Maximum-PC-Builds-Archive/welcome.gif` (5.3 MB) for re-encoding during the move rather than hot-linking at that size.

Two items still need your ruling at the Wave 0.5 sign-off gate, both legal rather than technical: the **12 GPL-3 coursework repos** (reads like a 2021 default, not intent), and the **14 transcript archives** — those are machine-generated derivatives of other people's recorded speech, so CC-BY-4.0 isn't yours to grant. The plan proposes MIT on the pipeline code plus a provenance notice on the transcript text.
  - `ExitPlanMode: # Documentation Standardization Across 125 Repos ## Context `D:\W\willtheorangeguy` holds 125 independent git repos accumulated over roughly a decade. Their doc`

**Claude:** Plan approved. Setting up tracking and starting Wave 0.
  - `ToolSearch: select:TaskCreate,TaskUpdate,TaskList`
  - `TaskCreate: Wave 0: Rewrite .github canonical health files`
  - `TaskCreate: Wave 0: Build .github/icons/ from 47 repo images`
  - `TaskCreate: Wave 0.6: Verify every icon URL resolves`
  - `TaskCreate: Wave 0.5: Generate 125-row classification table for sign-off`
  - `TaskCreate: Wave 1: Mechanical sweep across all 125 repos`
  - `TaskCreate: Wave 2: Pilot 3 repos end to end`
  - `TaskUpdate: 1`
  - `Read: D:\W\willtheorangeguy\.github\CODE_OF_CONDUCT.md`
  - `Read: D:\W\willtheorangeguy\.github\FUNDING.yml`
  - `Read: D:\W\willtheorangeguy\.github\PULL_REQUEST_TEMPLATE.md`

**Claude:** Before writing the canonical texts that all 125 repos will inherit, three things I can't derive:
  - `AskUserQuestion`

**Claude:** Decisions locked. Reading the issue templates, then writing the canonical set.
  - `Read: D:\W\willtheorangeguy\.github\ISSUE_TEMPLATE\bug-report.md`
  - `Read: D:\W\willtheorangeguy\.github\ISSUE_TEMPLATE\feature-request.md`
  - `Read: D:\W\willtheorangeguy\.github\ISSUE_TEMPLATE\question.md`

**Claude:** Now writing the canonical set. Starting with `SECURITY.md` and the license sources of truth:
  - `Write: D:\W\willtheorangeguy\.github\SECURITY.md`

**Claude:** Now the canonical license bodies — the source of truth for the Wave 1 sweep:
  - `Write: D:\W\willtheorangeguy\.github\licenses\MIT.md`
  - `PowerShell: $src="D:\W\willtheorangeguy\.github\LICENSE.md" "lines: " + (Get-Content $src | Measure-Object -Line).Lines Copy-Item $src "D:\W\willtheorangeguy\.github\licens`
  - `Edit: D:\W\willtheorangeguy\.github\licenses\CC-BY-4.0.md`
  - `Write: D:\W\willtheorangeguy\.github\licenses\README.md`

**Claude:** Now `CONTRIBUTING.md` — Discord references removed, support routed to Discussions:
  - `Write: D:\W\willtheorangeguy\.github\CONTRIBUTING.md`

**Claude:** Now the Code of Conduct — upgraded to Contributor Covenant 2.1, with the Discord enforcement contact replaced:
  - `Write: D:\W\willtheorangeguy\.github\CODE_OF_CONDUCT.md`

**Claude:** Now the templates. Converting issue templates to YAML forms gives better-structured reports:
  - `Write: D:\W\willtheorangeguy\.github\PULL_REQUEST_TEMPLATE.md`
  - `Write: D:\W\willtheorangeguy\.github\ISSUE_TEMPLATE\bug-report.yml`
  - `Write: D:\W\willtheorangeguy\.github\ISSUE_TEMPLATE\feature-request.yml`
  - `Write: D:\W\willtheorangeguy\.github\ISSUE_TEMPLATE\question.yml`
  - `Write: D:\W\willtheorangeguy\.github\ISSUE_TEMPLATE\config.yml`
  - `PowerShell: $p="D:\W\willtheorangeguy\.github\ISSUE_TEMPLATE" Remove-Item "$p\bug-report.md","$p\feature-request.md","$p\question.md" -Confirm:$false Get-ChildItem $p | Sel`

**Claude:** Now `LICENSE.md` for the `.github` repo itself, and its README in the new house style:
  - `PowerShell: Copy-Item "D:\W\willtheorangeguy\.github\licenses\MIT.md" "D:\W\willtheorangeguy\.github\LICENSE.md" -Force Get-Content "D:\W\willtheorangeguy\.github\LICENSE.m`
  - `Write: D:\W\willtheorangeguy\.github\README.md`

**Claude:** Health files done. Now building `icons/` — copying all 47 images with lowercased names:
  - `PowerShell: $base="D:\W\willtheorangeguy" $dest="$base\.github\icons" New-Item -ItemType Directory -Force -Path $dest | Out-Null $count=0 Get-ChildItem $base -Directory -Fo`

**Claude:** 18 repos (my plan said 20 — the correct figure is 18). Two loose images live directly in `docs/` rather than `docs/images/`. Let me catch those and check for re-encoding tools:
  - `PowerShell: "--- image tools ---" foreach ($t in @("ffmpeg","magick","cwebp")) { $c=Get-Command $t -ErrorAction SilentlyContinue; if($c){"$t : $($c.Source)"} else {"$t : NO`
  - `PowerShell: $dest="D:\W\willtheorangeguy\.github\icons" New-Item -ItemType Directory -Force -Path "$dest\incremental-clicker","$dest\wikipicture-web" | Out-Null Copy-Item "`

**Claude:** Now re-encoding the two oversized GIFs with ffmpeg:
  - `PowerShell: $d="D:\W\willtheorangeguy\.github\icons" foreach ($g in @("PyTricks-Archive","Maximum-PC-Builds-Archive")) { $in="$d\$g\welcome.gif" $out="$d\$g\welcome.mp4" ff`

**Claude:** MP4 won't render in a GitHub README (`<video>` isn't in their HTML allowlist). Optimizing the GIFs as GIFs instead:
  - `PowerShell: $d="D:\W\willtheorangeguy\.github\icons" foreach ($g in @("PyTricks-Archive","Maximum-PC-Builds-Archive")) { $in="$d\$g\welcome.gif" ffmpeg -hide_banner -i $in`

**Claude:** 1280×720 at 33fps — far more than a README hero needs. Downscaling to 800px/12fps with palette optimization:
  - `PowerShell: $d="D:\W\willtheorangeguy\.github\icons" foreach ($g in @("PyTricks-Archive","Maximum-PC-Builds-Archive")) { $in="$d\$g\welcome.gif" $pal="$env:TEMP\pal_$g.png"`

**Claude:** 12.95 MB is still too heavy for a README. Checking duration and going more aggressive:
  - `PowerShell: $d="D:\W\willtheorangeguy\.github\icons" foreach ($g in @("PyTricks-Archive","Maximum-PC-Builds-Archive")) { ffmpeg -hide_banner -i "$d\$g\welcome.gif" 2>&1 | S`

**Claude:** PyTricks-Archive is a 20-second animation. Going to 600px/8fps/64 colors:
  - `PowerShell: $d="D:\W\willtheorangeguy\.github\icons" $cfg=@{ "PyTricks-Archive"=@{w=600;fps=8;c=64}; "Maximum-PC-Builds-Archive"=@{w=800;fps=12;c=96} } foreach ($g in $cfg.`
  - `PowerShell: $d="D:\W\willtheorangeguy\.github\icons" foreach ($g in @("PyTricks-Archive","Maximum-PC-Builds-Archive")) { Remove-Item "$d\$g\welcome.mp4" -Force -ErrorAction`

**Claude:** Now the icons manifest, then I'll review what's staged:
  - `Write: D:\W\willtheorangeguy\.github\icons\README.md`
  - `PowerShell: cd "D:\W\willtheorangeguy\.github" "--- branch ---"; git rev-parse --abbrev-ref HEAD "--- remote ---"; git remote -v | Select-Object -First 1 "--- status ---";`

**Claude:** Everything as expected. Committing on a branch (not `main`):
  - `PowerShell: cd "D:\W\willtheorangeguy\.github" git switch -c docs/standardize git add -A git status --short`
  - `Bash: cd "D:/W/willtheorangeguy/.github" && git commit -q -F - <<'EOF' docs: rewrite canonical health files and centralize image assets Wave 0 of the documentation st`
  - `TaskUpdate: 1`
  - `TaskUpdate: 2`

**Claude:** Wave 0 is committed locally on `docs/standardize`. Before I push — the two GIFs were re-encoded, so worth eyeballing the quality:
  - `SendUserFile: Re-encoded hero GIFs. PyTricks-Archive: 23.2 MB → 6.3 MB (600px, 8fps, 64 colors — it's a 20-second animation, so it stayed the larger of the two). Maximum-PC-B`

**Claude:** **Wave 0 complete and committed locally** — 66 files changed on branch `docs/standardize` in `.github`.

**Health files**
- `SECURITY.md` — reporters now go through GitHub private vulnerability reporting instead of public issues. Added response targets (7/14/90 days), disclosure policy, and an explicit out-of-scope list.
- `CODE_OF_CONDUCT.md` — upgraded 2.0 → 2.1. The old enforcement contact was "the project's Discord," which no longer exists.
- `CONTRIBUTING.md` — rewritten, all Discord references gone, routed to Discussions/Issues.
- Issue templates converted from Markdown to **YAML forms** with required fields, plus a `config.yml` that steers security reports away from the tracker. The old PR template asked "what you expected to happen" twice and never asked what the PR actually did.

**Licensing** — `licenses/` now holds the canonical MIT and CC-BY-4.0 bodies plus `Copyright © 2026 willtheorangeguy`, and a table recording the repos that intentionally deviate. This is what the Wave 1 sweep will write out from.

**Icons** — 49 files from 20 repos (not 47/18 as the plan estimated; I found two loose images sitting directly in `docs/` in `incremental-clicker` and `wikipicture-web`). Total 11.9 MB, down from ~32 MB.

Three judgment calls you should know about:

1. **The COC enforcement contact is now `willtheorangeguy@outlook.com`.** With Discord dropped there was no private channel for conduct reports, and GitHub offers no COC equivalent of private vuln reporting. This publishes your email across all 125 repos via inheritance — say the word and I'll swap it for something else.
2. **`.github`'s own license is now MIT**, changed from CC-BY-4.0. That follows the plan's META-ORG rule, and MIT is friendlier for boilerplate people copy.
3. **The GIFs above** — PyTricks is a 20-second animation, so even at 600px/8fps it only got to 6.3 MB. If that still reads as too heavy for a README hero, the alternative is a static still with the GIF behind a link.

I've stopped short of pushing, since this is the first outward-facing step and all 125 repos inherit from it.
  - `AskUserQuestion`

**Claude:** Understood — I'll push the PR now and update the COC contact on the branch once you give me the address (it's a PR, so nothing is final until merge).
  - `PowerShell: cd "D:\W\willtheorangeguy\.github" gh auth status 2>&1 | Select-Object -First 5`

**Claude:** `gh` isn't authenticated. Let me try the plain git push first — credentials may be cached:
  - `PowerShell: cd "D:\W\willtheorangeguy\.github" git push -u origin docs/standardize 2>&1 | Select-Object -First 15`

**Claude:** Pushed. `gh` isn't authenticated, so open the PR here: **https://github.com/willtheorangeguy/.github/pull/new/docs/standardize**

Meanwhile, let me verify the icon assets actually resolve — testing against the pushed branch (the `/main/` URLs go live on merge):
  - `PowerShell: $base="https://raw.githubusercontent.com/willtheorangeguy/.github/docs/standardize/icons" $files = Get-ChildItem "D:\W\willtheorangeguy\.github\icons" -Recurse`

**Claude:** All 49 icon URLs return 200. That confirms the assets are intact and correctly pathed; the same URLs on `/main/` go live when the PR merges.
  - `TaskUpdate: 3`
  - `TaskUpdate: 4`

**Claude:** Now Wave 0.5 — the classification table. Building the detector:
  - `Write: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1`
  - `PowerShell: & "C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1"`

**Claude:** 125 repos classified, 27 needing your ruling. Let me pull the full table:
  - `PowerShell: $p="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classification.csv" Import-Csv $p | ForEac`

**Claude:** Before building the sign-off document, let me sanity-check a few classifications that look wrong:
  - `PowerShell: foreach ($r in @("deedown","Maximum-PC-Builds-Archive","llm-game-review-generator","aldec","internetspeed.travel","washroom-tracker.travel","proxmox-release-tra`

**Claude:** The `ARCHIVE-DATA` fallback bucket is catching real code repos. Also notable: the `.travel` repos already carry a `CONTENT_LICENSE.md` alongside `LICENSE.md` — a dual-license convention worth preserving.
  - `PowerShell: Get-Content "D:\W\willtheorangeguy\internetspeed.travel\CONTENT_LICENSE.md" -TotalCount 12 "---- README head ----" Get-Content "D:\W\willtheorangeguy\internetsp`

**Claude:** Confirmed — `LICENSE.md` (MIT) for code plus `CONTENT_LICENSE.md` (CC-BY-4.0) for data. That existing convention solves the transcript provenance problem cleanly. Let me fix the classifier and adopt it:
  - `Edit: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1`
  - `Edit: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1`

**Claude:** Now adding dual-license detection, which changes the target for mixed code+content repos:
  - `Edit: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1`
  - `Edit: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1`
  - `PowerShell: & "C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1" Write-Output "" Write-Output`

**Claude:** Two remaining issues: `*-Archive` repos are genuinely archives despite having a scraper, and the CC-BY→dual flag is a false alarm (the content license is preserved, not lost).
  - `Edit: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1`
  - `Edit: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1`
  - `PowerShell: & "C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classify.ps1" 2>&1 | Select-Object -First 2`

**Claude:** Classification is now clean — the true relicense list is 11 repos, all coursework. Let me pull the final data and build the sign-off document.
  - `PowerShell: $p="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\classification.csv" Import-Csv $p | ForEac`

**Claude:** I have the full dataset. Building the sign-off document as an artifact:
  - `Skill: artifact-design`

**You:** Approach this as the design lead at a small studio known for their versatility, giving every client a visual identity pitched at the treatment the task actually calls for. Make deliberate choices about palette, typography, and layout that are specific to this subject, and avoid templated designs.

## Read the request first

Calibrate treatment, not whether to design. A doc deserves the same craft as a landing page — what changes is the treatment that craft is delivered in.

Many requests call for a more utilitarian treatment: a plan, a memo, a demo. Make it polished: include real typographic hierarchy, considered spacing, and a proper palette, but avoid over-designing. Most pages do not need a flashy, gigantic hero. Keep flourishes tasteful and limited.

Some requests call for an editorial treatment: a landing page, a game, an app or tool they'll keep or share.

When unsure: a well-composed page is never the wrong answer; an over-designed visual identity sometimes is.

Fundamentals below apply to everything. The editorial process after that runs only when the read above says so.

## Fundamentals for every artifact

**Honor what's already there** Look for an existing design system first — CLAUDE.md, a tokens or theme file, existing component styles. When one exists, apply it; everything below fills gaps and never overrides. Precedence is always: the user's own words, then the project's existing system, then your choices.

**Ground it in the subject.** If the subject isn't already clear, pin it: one concrete subject, its audience, and the page's single job. The subject's own world — its materials, instruments, vernacular — is where distinctive choices come from. Build with real content throughout, never lorem.

**Pair typefaces** Typography carries the page even when the page isn't about typography. The Artifact CSP blocks font CDNs, so don't link a webfont URL and risk a silent fallback. Instead inline the face as a @font-face data URI. Keep running text near 65 characters wide; set a type scale and stay on it; give headings `text-wrap: balance`, body text room to breathe, and uppercase labels a touch of letter-spacing.

**Choose neutrals, don't default to them.** A pure mid-grey reads as unconsidered; a grey with a slight hue bias toward the page's accent reads as chosen. Pure white and near-black are fine grounds when they suit the subject — the point is that the neutral was picked, not inherited.

**Design both themes.** The page renders in the viewer's theme, and the viewer has three states, not two: an explicit choice stamps `data-theme="dark"` / `data-theme="light"` on the root element, and the default "system" setting stamps *nothing* — most viewers see the un-stamped document, where only `prefers-color-scheme` separates light from dark. Structure the CSS token-level for all three: the bare `:root` block defines the complete light palette (for a deliberately dark-first design, swap light and dark consistently through this whole pattern); `@media (prefers-color-scheme: dark)` redefines only the tokens, guarded as `:root:not([data-theme="light"])` so an explicit light choice beats a dark OS; `:root[data-theme="dark"]` redefines them again so the toggle also wins in the other direction. Style components through the tokens, never directly inside a media or `[data-theme]` block — a color whose only definition sits behind `[data-theme]` never applies in the un-stamped state, and the page renders one theme's text on the other theme's ground. Two more rules keep each theme resolving as a set: the artifact composites over a ground the viewer paints in *its* theme, so `body` must set an explicit `background` from a token — a transparent body silently borrows the host's ground; and every element that sets a color takes it from the same token set as the surface behind it, never a literal that only works in one theme. Before publishing, scan the stylesheet for any color declared only inside a media or `[data-theme]` block — that is the classic unreadable-artifact bug. Give the second theme the same care as the first — don't naively invert; keep contrast legible and the accent working on both grounds. A design that deliberately commits to one visual world (a neon arcade screen, a letterpress invitation) may stay single-theme — then skip the media query and stamps entirely but still paint the background and every color explicitly, so the page holds on either host ground; make it a choice, not an omission.

**Let layout do the spacing.** Lay out sibling groups with flex or grid and `gap`, not per-element margins that silently collapse or double. Wide content — tables, code, diagrams — gets `overflow-x: auto` on its own container so the page body never scrolls sideways. Reach for `font-variant-numeric: tabular-nums` wherever digits line up in columns.

**Avoid AI-generated design** AI-generated design currently clusters around a few looks: warm cream (#F4F1EA) with a serif display and terracotta accent; near-black with a lone acid-green or vermilion pop; broadsheet hairline rules with dense columns; a purple-to-blue gradient hero on white; Inter or Space Grotesk as the "safe" face; emoji as section markers; everything centered; `rounded-lg` everywhere; accent bar/rail on rounded cards. Where the user pins down a visual direction, follow it exactly — their words always win, including when they ask for one of these looks. Where nothing is specified, don't spend that freedom on one of these defaults.

**Build cleanly** Be cognizant of overlapping elements, cascade collisions, silent font fallbacks; visual bugs hide in the gap between source and output. Close every non-void element, double-quote attributes, give keyboard focus a visible state, respect `prefers-reduced-motion`. For generative or decorative graphics, reach for Canvas or WebGL rather than hand-authoring long SVG path data.

**CSS rules** When writing the CSS, watch your selector specificities. It is easy to generate classes that cancel each other out — a type-based selector like `.section` fighting an element-based one like `.cta` over padding and margins between sections. Structure the cascade so it doesn't silently undo your spacing.

**Writing the copy** Words are design material, not decoration. Write from the user's side of the screen — name things by what people recognize, not how the system is built (a person manages *notifications*, not *webhook config*). Active voice; a control says exactly what happens ("Publish", then a toast that says "Published"). Errors explain what went wrong and how to fix it — no apologies, no vagueness. Specific beats clever.

**Structure is information** Structural devices, numbering, eyebrows, dividers, labels, should encode something true about the content, not decorate it. Many generic designs use numbered markers (01 / 02 / 03), but that's only appropriate if the content actually is a sequence - like a real process or a typed timeline where order carries information the reader needs. Question if choices like numbered markers actually make sense before incorporating them.

**When it's a UI, not a document** A dashboard or tool is scanned and operated, not read top-to-bottom, so the craft shifts from typography to information design. Surface the summary before the detail; encode state in form as well as number — a pill, a chip, a severity stripe — so what needs attention reads at a glance. Semantic color (good / warning / critical) is separate from the accent hue and doesn't count as your accent. Give sparklines and charts the same care as type: an area fill, a faint grid, an emphasized endpoint. What's interactive should look interactive.



## Process

Before writing code, sketch a short design plan — a compact token system with color, type, and layout:
- **Color**: describe the palette as 4–6 named hex values.
- **Type**: typefaces for 2+ roles — a characterful display face used with restraint, a complementary body face, and a utility face for captions or data if needed.
- **Layout**: a layout concept in one or two sentences.

Then build, following the plan and deriving every color and type decision from it.

## When the request is editorial

The stance shifts: the client has already rejected proposals that felt templated, and is paying for a distinctive point of view. Make opinionated calls, and take one real aesthetic risk where it serves the work.

Review the design plan against the subject before building: if any part of it reads like the generic default you would produce for any similar page, revise that part, and note what you changed and why. Only after you've confirmed the plan's uniqueness do you write the code, following the revised plan exactly.

**Principles** 

- The hero is a thesis: open with the most characteristic thing in the subject's world — headline, image, live demo, interactive moment. 
- Typography carries the personality of the page. Pair the display and body faces deliberately, not the same families you would reach for on any other project, and set a clear type scale with intentional weights, widths, and spacing. Make the type treatment itself a memorable part of the design, not a neutral delivery vehicle for the content. 
- Leverage motion deliberately. Think about where and if animation can serve the subject: a page-load sequence, a scroll-triggered reveal, hover micro-interactions, ambient atmosphere. An orchestrated moment usually lands harder than scattered effects; choose what the direction calls for. However, sometimes less is more, and extra animation contributes to the feeling that the design is AI-generated. 
- Match complexity to the vision. Maximalist directions need elaborate execution; minimal directions need precision in spacing, type, and detail. Elegance is executing the chosen vision well.
- Spend your boldness in one place; keep everything around it quiet. If the accent fights the ground, shift it toward analogous or drop saturation rather than replacing it.
  - `Write: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave05-signoff.html`

**Claude:** Good — that unblocks the `/main/` icon URLs. Let me fix a CSS slip in the artifact before publishing:
  - `Edit: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave05-signoff.html`

**Claude:** Now re-verifying the icon URLs against `/main/`, since that's what all 125 READMEs will actually reference:
  - `PowerShell: $base="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons" $files = Get-ChildItem "D:\W\willtheorangeguy\.github\icons" -Recurse -File | Wher`

**Claude:** All 49 icon URLs live on `/main/`. Publishing the sign-off register:
  - `Artifact: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave05-signoff.html`
  - `TaskUpdate: 4`
  - `TaskUpdate: 5`

**Claude:** **Wave 0 is live** and all 49 icon URLs resolve on `/main/` — the asset layer 125 READMEs will depend on is confirmed working.

**Wave 0.5 register:** https://claude.ai/code/artifact/511a2327-52df-42d4-9e5c-538c6bd1fbb1

All 125 repos classified from file signatures — filterable by class, flag, branch, or licence state. Writing the detector surfaced things worth knowing:

**The fallback bucket was lying.** My first pass classified anything without a root manifest as `ARCHIVE-DATA` → CC-BY-4.0. That swept up real tools: `deedown` (shell scripts, no `.py` at root), `aldec` (`.pyw` files the `*.py` filter missed), `proxmox-release-tracker` (code in `scripts/`), `llm-game-review-generator` (a Flask app). All four would have been relicensed as content. Fixed with a recursive scan across 23 source extensions; `ARCHIVE-DATA` dropped from 8 repos to 5.

**You already solved the transcript problem.** `internetspeed.travel` and `washroom-tracker.travel` carry `LICENSE.md` (MIT) *plus* `CONTENT_LICENSE.md` (CC-BY-4.0). That's exactly the split the 14 transcript archives need — code and content licensed separately — so I've made it the convention rather than inventing one. It also means the plan's "MIT for code, CC-BY for content" decision becomes per-file rather than per-repo for mixed repos.

**The true relicense list is small.** Only 11 repos would have an existing licence genuinely replaced, and all 11 are coursework. Everything else is either already correct, unlicensed, or a dual-licence migration that preserves the existing terms.

Three decisions block Wave 1 — all on the artifact:

1. **11 coursework repos** GPL-3.0/CC-BY → MIT. Reversible only if nobody's forked, and you can't relicense group work you didn't solely author.
2. **14 transcript archives** — currently claiming blanket MIT over other people's recorded speech. Recommend a provenance notice in `CONTENT_LICENSE.md` rather than a CC grant, since CC isn't yours to give either.
3. **4 repos staying GPL-3.0** (`Craft-Clash`, `Python-Logo-Widgets`, `cv`, `deedown`) — confirm that's deliberate.

Two operational blockers for the 124-repo sweep: `gh auth login` (I can push via cached git credentials, but not open PRs), and `gh repo list --json name,visibility` — health-file deletion must skip private repos, since org-level `.github` defaults only reach public ones.

**You:** Leave the coursework repos at GPL-3.0, add the CONTENT_LICENSE.md to the transcript repos as suggested, and leave the four repos at GPL-3.0 that you suggested. I have logged in to gh, please also use it to check if any of the repos you are planning to do work to are archives  - if so, leave as is

**Claude:** Rulings noted. Let me check `gh` for archived repos and visibility — both change what Wave 1 touches.
  - `PowerShell: gh auth status 2>&1 | Select-Object -First 3 "--- repo metadata ---" gh repo list willtheorangeguy --limit 300 --json name,visibility,isArchived,isFork,defaultB`
  - `PowerShell: $f="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\ghmeta.tsv" $m = Get-Content $f | ForEach-`

**Claude:** This substantially changes Wave 1. Let me cross-tabulate against the health-file inventory:
  - `PowerShell: $base="D:\W\willtheorangeguy" $f="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\ghmeta.tsv"`

**Claude:** This changes Wave 1 materially. Let me record the findings in the plan before executing:
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`
  - `Edit: C:\Users\Daniela Sada\.claude\plans\this-folder-contains-all-dynamic-cupcake.md`

**Claude:** Now the transcript provenance notice — the one piece of new content Wave 1 needs:
  - `Write: D:\W\willtheorangeguy\.github\licenses\CONTENT_LICENSE-transcripts.md`

**Claude:** Now the Wave 1 sweep. First, the transcript sources for the provenance notice:
  - `PowerShell: foreach ($r in @("WAN-Transcripts","Oxide-and-Friends-Transcripts","HCC-Sermon-Transcripts","TBPN-Transcripts")) { "===== $r" Get-Content "D:\W\willtheorangeguy`

**Claude:** Now the Wave 1 sweep script, with a dry-run mode:
  - `Write: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave1.ps1`
  - `PowerShell: & "C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave1.ps1"`

**Claude:** Before applying — the plan requires asserting a clean tree and correct branch per repo. Let me check:
  - `PowerShell: $base="D:\W\willtheorangeguy" $scratch="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad" $meta`

**Claude:** 40 repos have uncommitted changes. I need to see what they are before sweeping over them:
  - `PowerShell: $base="D:\W\willtheorangeguy" foreach ($n in @("booking-scraper","PyWorkout","gflights-cli","YouTube-Description-Generator","Auto-Anouncements","docs")) { "====`

**Claude:** These are your own in-progress edits (source files, `pyproject.toml`). I won't touch them — but I need to know if any overlap the files Wave 1 writes:
  - `PowerShell: $base="D:\W\willtheorangeguy" $scratch="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad" $meta`

**Claude:** Zero overlap — Wave 1 can stage only its own files safely. First, syncing `.github` local state after your merge:
  - `PowerShell: cd "D:\W\willtheorangeguy\.github" git switch main 2>&1 | Select-Object -Last 2 git pull --ff-only 2>&1 | Select-Object -Last 3 "--- HEAD ---"; git log --onelin`
  - `PowerShell: cd "D:\W\willtheorangeguy\.github" git status --porcelain git add licenses/CONTENT_LICENSE-transcripts.md git commit -q -m "docs: add transcript provenance noti`

**Claude:** Now applying Wave 1 file changes across the 102 actionable repos (no git operations yet — the plan calls for reviewing the aggregate diff first):
  - `PowerShell: & "C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave1.ps1" -Apply`

**Claude:** Now the aggregate review before anything is committed:
  - `PowerShell: $base="D:\W\willtheorangeguy" $scratch="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad" $meta`

**Claude:** The untracked `.bandit`/`__pycache__` files are pre-existing, not mine. Counts reconcile. Let me spot-check the actual content:
  - `PowerShell: $b="D:\W\willtheorangeguy" "===== 1. Transcript provenance, source substituted (WAN-Transcripts)" Get-Content "$b\WAN-Transcripts\CONTENT_LICENSE.md" -TotalCoun`

**Claude:** All five checks pass. Now the git flow — piloting on 3 repos first to verify PR mechanics:
  - `Write: C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave1-git.ps1`
  - `TaskUpdate: 5`
  - `PowerShell: & "C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave1-git.ps1" -Only @("WAN-Transcripts","s`

**Claude:** Let me verify the pilot didn't disturb your in-flight work:
  - `PowerShell: $b="D:\W\willtheorangeguy" foreach ($n in @("PyWorkout","skyscanner-cli","WAN-Transcripts")) { "===== $n" " branch now : " + (git -C "$b\$n" rev-parse --abbrev-`

**Claude:** Pilot is clean — repos restored to `main`, your uncommitted work untouched, PRs contain only target files. Running the remaining 99:
  - `PowerShell: & "C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave1-git.ps1" 2>&1 | Select-Object -Last 4`

**Claude:** 96 succeeded, but let me check four anomalies:
  - `PowerShell: $scratch="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad" "=== non-ok statuses ===" Import-Cs`

**Claude:** Four distinct issues. Let me investigate the history divergence and permissions first:
  - `PowerShell: $b="D:\W\willtheorangeguy" foreach ($n in @("steamsizer","grammarly-md")) { "===== $n" " local HEAD root : " + (git -C "$b\$n" rev-list --max-parents=0 HEAD 2>$`

**Claude:** Diagnosis: `steamsizer` and `papers` look like transient PR failures (both have valid common history and ADMIN rights), but **`grammarly-md`'s local clone has a completely different root commit than its remote** — unrelated histories. Let me fix what I can:
  - `PowerShell: $b="D:\W\willtheorangeguy" $msg="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave1-msg.txt`

**Claude:** Both persist. Let me look at what's actually on the remotes:
  - `PowerShell: $b="D:\W\willtheorangeguy" "===== steamsizer" " local docs/standardize : " + (git -C "$b\steamsizer" rev-parse docs/standardize 2>&1) " remote docs/standardize`

**Claude:** `steamsizer`'s remote `main` was force-pushed since your last local fetch (`6119a23` vs local `af6f745`) — my branch was built on orphaned history. `papers` has Issues disabled, which blocks PR creation. Let me fix both:
  - `PowerShell: $b="D:\W\willtheorangeguy" "===== steamsizer: fetch current remote state" git -C "$b\steamsizer" fetch origin 2>&1 | Select-Object -Last 2 " uncommitted (must p`

**Claude:** You've hit your session limit · resets 2:10pm (America/Vancouver)

**You:** tokens have reset please continue where you left off

**Claude:** `steamsizer`'s local clone is orphaned from its remote — no merge-base at all. That's a repo-state problem I shouldn't force-resolve. Cleaning up my branch there and leaving it as found:
  - `PowerShell: $b="D:\W\willtheorangeguy" "=== steamsizer: remove the unmergeable branch, restore repo as found ===" git -C "$b\steamsizer" switch main 2>&1 | Select-Object -L`

**Claude:** Now the three `KEEP` repos whose renames were staged but never committed, and the profile repo that wrongly received a license:
  - `PowerShell: $b="D:\W\willtheorangeguy" $msg="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\wave1-msg.txt`

**Claude:** Now reverting the profile repo — the plan specified no license there, but the sweep's fallback added one:
  - `PowerShell: $b="D:\W\willtheorangeguy" "=== whisper-captions: upstream copyright preserved? ===" Get-Content "$b\whisper-captions\LICENSE.md" -TotalCount 3 "" "=== willtheo`

**Claude:** The file is on the branch, not `main` — that's correct. Verifying via the PR:
  - `PowerShell: "=== whisper-captions PR: upstream copyright must be preserved ===" gh pr diff 11 -R willtheorangeguy/whisper-captions 2>&1 | Select-Object -First 12 "" "=== cv`

**Claude:** Pure 100%-similarity renames — GPL and upstream copyright bodies untouched. Now a final verification sweep:
  - `PowerShell: $b="D:\W\willtheorangeguy" $scratch="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad" $meta=@{`
  - `TaskUpdate: 5`

**Claude:** **Wave 1 swept — 98 PRs open**, every repo restored to its default branch with your in-flight work untouched.

| | |
|---|---|
| Repos on disk | 125 |
| Archived → skipped | 20 |
| Deferred to manual | 3 (`aibot`, `notes`, `.github`) |
| **PRs opened** | **98** |
| Exceptions | 4 |

**What each PR does:** normalizes the license body and copyright line to `Copyright © 2026 willtheorangeguy`, renames extensionless `LICENSE` → `LICENSE.md`, adds `CONTENT_LICENSE.md` where a repo carries both code and content, deletes duplicated health files from public repos, and rewrites the README links to those files to absolute `.github` URLs *in the same commit* so nothing dangles.

Your rulings held: the four GPL-3.0 repos and the vendored Apache/BSD/upstream ones came through as **100%-similarity renames** — filename changed, license body byte-identical. All 13 coursework repos were archived anyway, so that question resolved itself.

**Four things didn't go clean:**

1. **`steamsizer`** — its remote `main` was force-pushed to an unrelated history since your last fetch (`af6f745` → `6119a23`, no merge-base). My branch was built on orphaned commits and could never merge. I deleted it locally and remotely and left the repo exactly as found. **Your local clone is orphaned from GitHub** — worth resolving before it gets further out of sync.
2. **`grammarly-md`** — same class of problem, different root commit entirely. Branch is pushed but unmergeable.
3. **`papers`** — has Issues disabled, which blocks `CreatePullRequest` via the API. Branch is pushed; merge it in the UI or I can push straight to `main`.
4. **`willtheorangeguy`** (profile) — the sweep's fallback added an MIT license, but the plan specified none for the profile card. PR closed, branch deleted, file removed.

One caveat on the 40 repos with uncommitted work: I staged only my seven target filenames, never `git add -A`. I verified beforehand that zero dirty files overlapped that set, and confirmed after the pilot that your edits survived intact.

Nothing is merged yet — 98 PRs are sitting open for review.
  - `AskUserQuestion`

**Claude:** Re-cloning the two orphaned repos fresh from GitHub, leaving your local clones untouched:
  - `PowerShell: $s="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\reclone" New-Item -ItemType Directory -For`
  - `PowerShell: $s="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\reclone" New-Item -ItemType Directory -For`

**Claude:** Both cloned at current remote HEAD. Applying Wave 1 changes and opening PRs:
  - `PowerShell: $s="C:\Users\DANIEL~1\AppData\Local\Temp\claude\D--W-willtheorangeguy\a5bbc541-1dc4-41e0-ab8d-40111d08a401\scratchpad\reclone" $msg="C:\Users\DANIEL~1\AppData\L`

**Claude:** Both re-cloned repos now have clean PRs. **Wave 1 total: 100 PRs open.** (`papers` still can't take a PR — its branch is pushed if you want to merge it in the UI.)

Moving to Wave 2. Let me read the pilot repos:
  - `Read: D:\W\willtheorangeguy\PyWorkout\README.md`
  - `PowerShell: $d="D:\W\willtheorangeguy\PyWorkout\docs" foreach ($f in @("README.md","USAGE.md","COMMANDS.md","CUSTOMIZATION.md")) { "########## $f (" + ((Get-Content "$d\$f"`

**Claude:** The existing `USAGE.md` references `send.exe`/`send.py` — copy-paste from another project; PyWorkout's entry is `main.py`. I'll fix that in the migration. Building Wave 2 stacked on the Wave 1 branch:
  - `PowerShell: $p="D:\W\willtheorangeguy\PyWorkout" git -C $p switch docs/standardize 2>&1 | Select-Object -Last 1 git -C $p switch -c docs/content 2>&1 | Select-Object -Last`
  - `Write: D:\W\willtheorangeguy\PyWorkout\README.md`
  - `Read: D:\W\willtheorangeguy\PyWorkout\README.md`

**Claude:** Confirmed Wave 1's link rewrite is present. Writing the Wave 2 README:
  - `Write: D:\W\willtheorangeguy\PyWorkout\README.md`

**Claude:** Now the `docs/` folder. Index and installation first:
  - `Write: D:\W\willtheorangeguy\PyWorkout\docs\README.md`
  - `Write: D:\W\willtheorangeguy\PyWorkout\docs\installation.md`
  - `Write: D:\W\willtheorangeguy\PyWorkout\docs\usage.md`

**Claude:** Now the case-sensitivity hazard from the plan. Let me check what actually happened on disk:
  - `PowerShell: $d="D:\W\willtheorangeguy\PyWorkout\docs" "=== actual filenames on disk ===" [System.IO.Directory]::GetFiles($d) | ForEach-Object { Split-Path $_ -Leaf } "" "==`

**Claude:** Exactly the hazard the plan flagged: disk says `usage.md`, but **git still tracks `docs/USAGE.md`** — committing now would leave the file uppercase in the repo and my README link would 404 on GitHub's case-sensitive filesystem. Fixing with two-step renames:
  - `PowerShell: $p="D:\W\willtheorangeguy\PyWorkout" # Two-step git mv: a direct case-only rename is a silent no-op on Windows. git -C $p mv docs/USAGE.md docs/usage.tmp 2>&1 |`

**Claude:** Git now tracks the renames correctly. Updating headings and cross-references in the migrated files:
  - `Edit: D:\W\willtheorangeguy\PyWorkout\docs\commands.md`
  - `Edit: D:\W\willtheorangeguy\PyWorkout\docs\configuration.md`
  - `PowerShell: $d="D:\W\willtheorangeguy\PyWorkout\docs" "=== configuration.md: 'Change the Videos' section ===" Get-Content "$d\configuration.md" | Select-Object -Skip 48 ""`
  - `Edit: D:\W\willtheorangeguy\PyWorkout\docs\testing.md`
  - `Edit: D:\W\willtheorangeguy\PyWorkout\docs\configuration.md`

**Claude:** Now `development.md`, the one genuinely new page — drawn from the repo's actual tooling:
  - `Write: D:\W\willtheorangeguy\PyWorkout\docs\development.md`

**Claude:** Now the plan's verification checks against this pilot:
  - `PowerShell: $p="D:\W\willtheorangeguy\PyWorkout" "1. README length: " + ((Get-Content "$p\README.md" | Measure-Object -Line).Lines) + " (budget 120)" "" "2. Nav anchors vs`

**Claude:** Two items: a `LICENSE.md` link in `commands.md` needs `../`, and my check-5 regex errored so may have masked others. Let me fix and re-verify properly:
  - `PowerShell: Select-String -Path "D:\W\willtheorangeguy\PyWorkout\docs\commands.md" -Pattern 'LICENSE' | ForEach-Object { "line $($_.LineNumber): $($_.Line)" }`

**Claude:** The doc says the `license` command shows **GNU GPL v3**, but PyWorkout is MIT. Let me check what the code actually prints:
  - `PowerShell: $p="D:\W\willtheorangeguy\PyWorkout" "=== what main.py prints for 'license' ===" Select-String -Path "$p\main.py" -Pattern 'license' -Context 0,6 | Select-Objec`

**Claude:** `commands.md` has no markdown links at all — my earlier check-5 hit was a false positive from the broken regex. But I found a real inconsistency: `main.py` prints **GPL boilerplate** ("ABSOLUTELY NO WARRANTY… free software… redistribute under certain conditions") while the repo is MIT-licensed. Fixing the doc to be accurate:
  - `Edit: D:\W\willtheorangeguy\PyWorkout\docs\commands.md`

**Claude:** Re-running verification with a corrected link checker:
  - `PowerShell: $p="D:\W\willtheorangeguy\PyWorkout" $bad=@() Get-ChildItem "$p\docs" -Filter *.md | ForEach-Object { $dir=$_.DirectoryName; $nm=$_.Name foreach ($m in [regex]`

**Claude:** All checks pass. Committing the pilot:
  - `Bash: cd "D:/W/willtheorangeguy/PyWorkout" && git add -A docs README.md && git commit -q -F - <<'EOF' docs: rewrite README and restructure docs/ to the house contract`
  - `PowerShell: $p="D:\W\willtheorangeguy\PyWorkout" git -C $p push -q -u origin docs/content 2>&1 | Select-Object -Last 2 $body = @" Wave 2 pilot for the documentation standar`
  - `TaskUpdate: 6`

**Claude:** **Wave 2 pilot 1 of 3 done — PyWorkout: https://github.com/willtheorangeguy/PyWorkout/pull/219** (stacked on Wave 1's #218, so merge that first).

README went **193 → 73 lines** against the 120 budget. `docs/` is now seven lowercase files: `README`, `installation`, `usage`, `commands`, `configuration`, `development`, `testing`.

The case-rename hazard from the plan **fired exactly as predicted**. Writing `docs/usage.md` on Windows silently renamed `USAGE.md` on disk while git still tracked it as uppercase — committing that would have left the file uppercase in the repo and my `docs/usage.md` link would have 404'd on GitHub, which *is* case-sensitive. Caught it with a filesystem-vs-git comparison and fixed all four renames via the two-step `git mv`.

Four content bugs surfaced while migrating, all pre-existing:

1. **Neither the logo nor the hero image has been rendering** — both used `github.com/.../blob/...`, which serves an HTML page. Now on `.github/icons` and verified 200.
2. **`docs/USAGE.md` documented running `send.exe` and `send.py`** — those belong to a different project. PyWorkout's entry point is `main.py`.
3. **`docs/COMMANDS.md` claimed the `license` command prints GNU GPL v3 text**, but the repo is MIT.
4. Several self-links shaped `/PyWorkout/main/README.md#git` were missing `/blob/`.

One thing I found but deliberately **did not** fix: `main.py` prints GPL boilerplate — *"ABSOLUTELY NO WARRANTY… free software… redistribute under certain conditions"* — while the repo is MIT-licensed, with a copyright line reading 2021-2024. That's a licensing decision rather than a docs one, so I flagged it in the PR and left the code alone. Same family of drift as the GPL-on-coursework you already ruled on.

Verification passed clean: 73 lines, no orphan nav anchors, no `Changelog`/`You may also like`, zero broken relative links in README or `docs/`, no lingering `docs/images` references, both image URLs 200.

Worth you looking at #219 rendered on GitHub before I replicate the pattern — the plan says freeze the template only after the pilots look right, and `treklogger` (API + DB schema split) and `WAN-Transcripts` (provenance, 7.1k files) exercise different parts of it. Say the word and I'll do both.
