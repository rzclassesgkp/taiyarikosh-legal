# Public legal pages (for Google Play / Razorpay)

Plain static HTML, English + Hindi on one page (language button top-right). No scripts from other sites.
`build.py` regenerates the pages from the same text as `src/pages/Legal.tsx`; edit the text there/here, then run
`python legal-site/build.py`.

| Page | File |
|---|---|
| Home | `index.html` |
| Privacy Policy (give this URL to Play Console) | `privacy.html` |
| Terms of Use | `terms.html` |
| Refund & Cancellation | `refund.html` |
| Delete account (Play "account deletion" URL) | `delete-account.html` |
| Contact & Grievance Officer | `contact.html` |

## Publish on GitHub Pages
GitHub Pages is only free for PUBLIC repositories, and the app repository is private, so these pages live in a
separate public repository that contains only this folder's files:

1. github.com -> New repository -> name e.g. `supertet-legal` -> **Public** -> Create.
2. Push the files (`index.html`, `privacy.html`, `terms.html`, `refund.html`, `delete-account.html`).
3. Repository -> Settings -> Pages -> Source: *Deploy from a branch* -> `main` / `/ (root)` -> Save.
4. After about a minute the pages are at `https://<github-username>.github.io/supertet-legal/privacy.html` etc.

The contact email shown on the pages is set at the top of `build.py` (`EMAIL`).
