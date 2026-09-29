# Monthly static website publication

## One-time activation

After the validation pull request is green and merged:

1. In this repository open **Settings → Pages → Build and deployment**.
2. Set **Source** to **GitHub Actions**. This prevents the old branch-based builder from publishing a competing, browser-fetching version.
3. Open **Actions → Monthly website publication → Run workflow**, select `master`, and leave **publish** enabled for the first static deployment.

No additional token is required. The workflow uses the repository's automatically provided `GITHUB_TOKEN`. It does not read or change the Overleaf token, the CV automation repository, or the Google Sheet.

## Schedule

`17 13 1 * *` starts a build at **13:17 UTC on the first day of every month**: 09:17 in Montréal during daylight saving time, 08:17 during standard time. Publication follows the successful build and tests; GitHub schedules are best-effort, not exact-time delivery guarantees.

There is deliberately **no push-to-production trigger**. Source changes wait for the next monthly build unless the owner manually runs the workflow. Pull requests run the build and checks but can never deploy. A manual run with `publish` unchecked is a dry run.

GitHub can disable scheduled workflows in a public repository after 60 days without repository activity. Spreadsheet edits are not repository activity. If disabled, re-enable this workflow from Actions. This workflow does not create artificial keep-alive commits.

## Build-time data flow

Google Sheet → validated Python rendering → existing Jekyll layout → complete static HTML → browser smoke tests → GitHub Pages artifact.

The action reads the existing `homepage`, `news`, `publications`, `grants`, `HQPs`, `teaching`, and `software` tabs once per build. It never scrapes the already published website as a data source.

`site.py prepare` replaces only the data-driven sections in the runner's temporary checkout and removes their browser-time Sheets scripts. It does not commit generated pages or rewrite the source repository. The original layouts, CSS, images, PDF files, page URLs, and manual text remain in the source. This lets the conversion preserve the existing design without replacing all the site's templates in one migration.

The published pages contain the finished content, including News and Publications. Visitors do not need JavaScript or access to Google Sheets to read that content. The theme may still use JavaScript for its mobile navigation; that is unrelated to data fetching.

## Content rules preserved

- Homepage prose is joined from the exact `homepage` text/link fragments, including meaningful spaces. It is not summarized or inferred from CV metadata.
- Institution links remain clickable in the biography/background. The position headline remains plain text, per the owner's preference.
- Projects respect the live `grants.in_website` checkbox. Neither aggregate funding totals nor individual amounts are displayed.
- PhD alumni precede master's and bachelor's alumni. Degree and completion status come from `HQPs`.
- Software contains only `Libraries & Tools` and `Datasets`, respects `in_website` and `sort_order`, and does not resurrect deleted rows.
- Talks and Academic do not reappear in the main menu or as their former page routes.
- CV generation and the website's existing PDF CV download are unchanged. This workflow does not compile or refresh that PDF.

## Safety gates

The workflow refuses to publish on a failed download, HTML/login response, malformed/missing headers, invalid visibility flag, spreadsheet formula error, missing required homepage section, duplicate homepage section/order, unsafe link, empty public section, lost records, missing existing assets, inconsistent navigation, or browser-time Sheets code remaining in the finished pages.

All source sections are prepared before writing any of them. All publication jobs depend on successful generation, Jekyll compilation, content checks, and browser tests. A failed build does not upload a replacement for deployment, so the previous live site remains in place. A deliberately emptied public section needs a reviewed code/configuration change instead of silently replacing a working page with nothing.

Validation checks URL syntax and the preserved homepage links, not the continued availability of every external university, publication, or software server.

Each successful build records counts and a timestamp in `/website-build.json`. Raw spreadsheet CSVs, internal tracker fields, build scripts, and the full validation report are not placed on the public website. The workflow retains a separate validation artifact with reports and desktop/mobile screenshots for 35 days, and its deployable site artifact for 7 days.

## Tests and debugging

```sh
python -m pip install -r _automation/requirements.txt
python -m unittest discover -s _automation -p 'test_*.py' -v
python _automation/site.py prepare
# Build the site with Jekyll into _site, then:
python _automation/site.py verify
python -m playwright install chromium
python _automation/browser_check.py
```

Run `prepare` only in a disposable checkout: it intentionally changes local page files for compilation. GitHub Actions provides that disposable checkout automatically.

If a scheduled run fails, inspect its first failing step and validation artifact. Fix the source/Sheet and manually run again. Do not bypass validation to force publication. Source changes can be reverted with an ordinary Git revert; restoring old source alone does not restore previous Sheet values, which have their own Google Sheets version history.
