# DISC-02: License and data-terms review

Reviewed 2026-11-25. This is a desk review of public repository files and published terms, not
legal advice; D1 (no TMDB) is unchanged. Upstream repositories are pinned to the latest
default-branch commit returned by GitHub on the review date. Where a source host could not be
fetched directly, quoted clauses were checked in its indexed public-page preview; confirm the
live source text and actual account contract before production use. Public terms may change.
“Not stated” means no relevant clause was found in the cited public source; it is not permission.

## Upstream license and contribution review

| Project | Inspected commit | SPDX / LICENSE path | NOTICE, CLA, and contribution obligations |
|---|---|---|---|
| [PenguWatch](https://github.com/pengupowered/penguwatch) | [`c8db48dafef64346caad966aed6e26236208b9fe`](https://github.com/pengupowered/penguwatch/commit/c8db48dafef64346caad966aed6e26236208b9fe) | MIT — [`LICENSE`](https://github.com/pengupowered/penguwatch/blob/c8db48dafef64346caad966aed6e26236208b9fe/LICENSE) | [`CONTRIBUTING.md`](https://github.com/pengupowered/penguwatch/blob/c8db48dafef64346caad966aed6e26236208b9fe/CONTRIBUTING.md) says, “By contributing you agree that your contribution is licensed under the project's MIT license.” No separate CLA or root NOTICE was found in the inspected root/`.github` listings. |
| [Sofa](https://github.com/jakejarvis/sofa) | [`a8294d977b0f2c0ad267d0b516298881a5571e86`](https://github.com/jakejarvis/sofa/commit/a8294d977b0f2c0ad267d0b516298881a5571e86) | MIT — [`LICENSE`](https://github.com/jakejarvis/sofa/blob/a8294d977b0f2c0ad267d0b516298881a5571e86/LICENSE) | No root `CONTRIBUTING.md`, NOTICE, or CLA found in the inspected root/`.github` listings. |
| [Findarr](https://github.com/Lillifee/findarr) | [`21652216e0390fae7644ae8de528e4365d0296e7`](https://github.com/Lillifee/findarr/commit/21652216e0390fae7644ae8de528e4365d0296e7) | MIT — [`LICENSE`](https://github.com/Lillifee/findarr/blob/21652216e0390fae7644ae8de528e4365d0296e7/LICENSE) | No root `CONTRIBUTING.md`, NOTICE, or CLA found in the inspected root/`.github` listings. |
| [Streamline](https://github.com/abhichandra21/streamline) | [`edc85337f73db626f6259372be69e0ad17d83394`](https://github.com/abhichandra21/streamline/commit/edc85337f73db626f6259372be69e0ad17d83394) | MIT — [`LICENSE`](https://github.com/abhichandra21/streamline/blob/edc85337f73db626f6259372be69e0ad17d83394/LICENSE) | [`CONTRIBUTING.md`](https://github.com/abhichandra21/streamline/blob/edc85337f73db626f6259372be69e0ad17d83394/CONTRIBUTING.md) says, “By contributing, you agree that your contributions are licensed under the MIT License.” No separate CLA or root NOTICE was found in the inspected root/`.github` listings. |
| [MediaShelf](https://github.com/ghltshubh/mediashelf) | [`6e49e62493ac9e12697f8186a94348f590963402`](https://github.com/ghltshubh/mediashelf/commit/6e49e62493ac9e12697f8186a94348f590963402) | AGPL-3.0-or-later — [`LICENSE`](https://github.com/ghltshubh/mediashelf/blob/6e49e62493ac9e12697f8186a94348f590963402/LICENSE) | No root `CONTRIBUTING.md`, NOTICE, or CLA found in the inspected root/`.github` listings. The copyleft license applies if reusing the software; an API integration does not itself grant rights to embed its code. |
| [MultiStream](https://github.com/renaudallard/multistream) | [`178554e46c4be843cebb2c10d3a1e89b797c2fce`](https://github.com/renaudallard/multistream/commit/178554e46c4be843cebb2c10d3a1e89b797c2fce) | NOASSERTION — no root `LICENSE` file found in the inspected tree. | No root `CONTRIBUTING.md`, NOTICE, or CLA found in the inspected root/`.github` listings. [`README.md`](https://github.com/renaudallard/multistream/blob/178554e46c4be843cebb2c10d3a1e89b797c2fce/README.md) contains legal/personal-use language, not a software license grant; do not reuse without permission. |
| [Yamtrack](https://github.com/FuzzyGrim/Yamtrack) | [`437a93240aa09eec4d0e3c31f6fbd6359462e92b`](https://github.com/FuzzyGrim/Yamtrack/commit/437a93240aa09eec4d0e3c31f6fbd6359462e92b) | AGPL-3.0-or-later — [`LICENSE`](https://github.com/FuzzyGrim/Yamtrack/blob/437a93240aa09eec4d0e3c31f6fbd6359462e92b/LICENSE) | No root `CONTRIBUTING.md`, NOTICE, or CLA found in the inspected root/`.github` listings. |
| [recommenders](https://github.com/recommenders-team/recommenders) | [`cc47866b0599721f8544d1cc850a5a1db091acb3`](https://github.com/recommenders-team/recommenders/commit/cc47866b0599721f8544d1cc850a5a1db091acb3) | MIT — [`LICENSE`](https://github.com/recommenders-team/recommenders/blob/cc47866b0599721f8544d1cc850a5a1db091acb3/LICENSE) | [`CONTRIBUTING.md`](https://github.com/recommenders-team/recommenders/blob/cc47866b0599721f8544d1cc850a5a1db091acb3/CONTRIBUTING.md) requires signed commits (“make sure you sign the commits, otherwise the tests will fail”). No separate CLA or root NOTICE found in the inspected root/`.github` listings; `AUTHORS.md` is present, not a NOTICE. |

The MIT license requires retaining its copyright and permission notice in copies or substantial
portions. The two AGPL repositories carry the AGPL-3.0-or-later text. The listings checked were
the repository roots and `.github` directories; nested package-specific licenses were not
exhaustively audited.

## Public data and API terms

Each source was reviewed on 2026-11-25. The quoted clause is the evidence; a silent source is
explicitly marked “not stated.” “Imagery” concerns rights to display or redistribute the image,
not whether an API happens to return an image URL.

### Streaming Availability API (Movie of the Night)

Primary source: [Terms & Conditions](https://developers.movieofthenight.com/terms-and-conditions), retrieved 2026-11-25.

| Dimension | Quoted clause / finding |
|---|---|
| Caching and retention | “The API User may cache and store the data and images retrieved via the Service locally, for as long as required by the functional needs of their application or use case, subject to these Terms.” After a subscription ends, “the API User may retain and continue using the data and images retrieved during the subscription period,” subject to the Terms and attribution. No fixed cache TTL is stated. |
| ML/AI use | Prohibited use includes: “Using the data provided via the Service to train, fine-tune, evaluate, or improve machine learning models or artificial intelligence systems.” Do not use any MotN payload to train, fine-tune, evaluate, or improve the ranker or another ML/AI system. |
| Attribution | When displaying both availability and images, attribution must state “the streaming availability metadata and images are provided by Streaming Availability API by Movie of the Night” and include a link to `https://www.movieofthenight.com/about/api`. Availability-only and image-only displays have their own corresponding required wording; see Decision inputs below. |
| Imagery rights | The Terms define posters, backdrops, artwork, logos, and some descriptions as third-party content and say: “The API Provider does not grant, and is not in a position to grant, any license or other right to use Third-Party Content.” Images are not cleared for display or redistribution merely because the API returns them; obtain the rights or omit them. |
| Commercial restrictions | The provider grants a right to use data “in applications, websites, or other software products, including commercial and consumer-facing products,” excluding third-party content and subject to the Terms. |
| Redistribution | “The API User shall not resell, sublicense, redistribute, publish, or otherwise make the data available as a standalone data product, API, database, or service,” or where the primary purpose is providing availability data to third parties. |

### Watchmode

Primary public sources: [Watchmode API plans](https://api.watchmode.com/) and [API documentation](https://api.watchmode.com/docs), retrieved 2026-11-25. The public plan page publishes plan conditions; a separate account-specific contract was not inspected.

| Dimension | Quoted clause / finding |
|---|---|
| Caching and retention | The public page says free-plan users “should refresh or delete cached data within 30 days.” It says paid subscribers may keep data in their own systems while the subscription is active, with “no fixed expiration,” if it is “only used within their own website or app and kept reasonably current.” |
| ML/AI use | Not stated in the cited public plan page or API documentation. |
| Attribution | The plan matrix states “Non-commercial, with attribution” for the free Developer plan and “Commercial, no attribution” for paid tiers. The exact required attribution wording and placement are not stated. |
| Imagery rights | The API documentation describes poster and backdrop art as available metadata, but the cited public plan page/docs do not state a separate image license or image-specific redistribution right. Not stated. |
| Commercial restrictions | The public plan matrix states free use is “Non-commercial, with attribution”; paid tiers list “Commercial, no attribution.” Confirm the applicable plan and account contract before commercial use. |
| Redistribution | No general redistribution license is stated. The paid-plan statement limits use to “their own website or app”; do not treat that as permission to resell or publish a standalone data product. |

### TVmaze

Primary source: [TVmaze API terms and documentation](https://www.tvmaze.com/api), retrieved 2026-11-25.

| Dimension | Quoted clause / finding |
|---|---|
| Caching and retention | “All output is cached by our HTTP load balancers for 60 minutes.” For images: “Images can safely be cached indefinitely” because a specific image URL’s content will not change. No maximum local retention period for API data is stated. |
| ML/AI use | Not stated as a specific use in the API documentation. The data license is CC BY-SA; do not infer an ML-specific grant or settle how ShareAlike applies to derived model artifacts from this silence. |
| Attribution | “You are free to directly link (‘hotlink’) to our image CDN.” For data attribution, “You can satisfy the attribution requirement by linking back to TVmaze from within your application or website.” No mandatory exact text is stated. |
| Imagery rights | The API documentation describes image URLs and caching, but does not state a separate image-specific rights grant in the cited clauses. Not stated separately; verify image rights before serving images. |
| Commercial restrictions | The API page says the data “can freely be used for any purpose” provided TVmaze is credited and the ShareAlike provision is followed. |
| Redistribution | The API page identifies CC BY-SA and requires ShareAlike compliance. Attribute TVmaze and preserve the applicable license when sharing adapted material; ask counsel whether particular derived fields are adaptations. |

### Wikidata structured data

Primary source: [Wikidata:Licensing](https://www.wikidata.org/wiki/Wikidata:Licensing), retrieved 2026-11-25.

| Dimension | Quoted clause / finding |
|---|---|
| Caching and retention | Not stated in the licensing page. API/dump etiquette and operational limits are separate from license retention rights. |
| ML/AI use | No ML/AI-specific clause is stated. The page says the structured data is CC0; it does not separately discuss model training. |
| Attribution | The page says “All structured data … is released into the public domain under Creative Commons Zero.” CC0 does not impose an attribution condition; a “Wikidata” source credit is still useful for provenance, but is not a license requirement. |
| Imagery rights | The CC0 statement is for structured data, not linked media. A Wikidata image property points to a separate file whose own license must be checked. |
| Commercial restrictions | No non-commercial restriction is stated for the CC0 structured data. |
| Redistribution | The cited page releases structured data under CC0; no redistribution restriction is stated for that structured data. |

### Wikipedia text (CC BY-SA)

Primary sources: [Wikipedia copyrights](https://en.wikipedia.org/wiki/Wikipedia:Copyrights) and [CC BY-SA 4.0 license text](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License), retrieved 2026-11-25.

| Dimension | Quoted clause / finding |
|---|---|
| Caching and retention | Not stated in the cited copyright/license terms. |
| ML/AI use | Not stated as a specific use in the cited copyright/license terms. The license grants reuse subject to its conditions; it does not explicitly settle model training or the licensing of model outputs. |
| Attribution | CC BY-SA requires identification of the creator, copyright notice, license notice, disclaimer notice, and a URI or hyperlink to the material “to the extent reasonably practicable.” Wikipedia’s reuse guidance says a link to the article is generally sufficient attribution. |
| Imagery rights | Article text terms do not establish image rights. Wikipedia says some images are under separate licenses; check each file’s license and restrictions independently. |
| Commercial restrictions | CC BY-SA 4.0 permits sharing “for any purpose, even commercially,” subject to attribution and ShareAlike. |
| Redistribution | The license allows copying and redistribution; “if You remix, transform, or build upon the material, You must distribute Your contributions under the same license as the original.” Do not assume that extracted numeric features or model artifacts are outside this condition; their status is not resolved here. |

### IMDb non-commercial datasets

Primary source: [IMDb: Can I use IMDb data in my software?](https://help.imdb.com/article/imdb/general-information/can-i-use-imdb-data-in-my-software/G5JTRESSHJBBHTGX), retrieved 2026-11-25.

| Dimension | Quoted clause / finding |
|---|---|
| Caching and retention | Not stated in the cited dataset-use help page. Dataset refresh cadence, if any, is not a local retention permission. |
| ML/AI use | Not stated specifically. Do not treat silence as permission; the use restriction below remains applicable. |
| Attribution | Not stated in the cited dataset-use clause. |
| Imagery rights | Not stated in the dataset-use clause; it does not grant rights to IMDb poster/still imagery. |
| Commercial restrictions | “The data can only be used for personal and non-commercial use.” |
| Redistribution | The same clause says data “must not be altered/republished/resold/repurposed to create any kind of online/offline database of movie information (except for individual personal use).” Do not include IMDb datasets in a shared catalog or product without separate permission. |

### MovieLens 32M and Tag Genome

Primary sources: [MovieLens 32M README](https://files.grouplens.org/datasets/movielens/ml-32m-README.html), [standalone Tag Genome README](https://files.grouplens.org/datasets/tag-genome/README.html), and [GroupLens dataset listing](https://grouplens.org/datasets/movielens/), retrieved 2026-11-25. The standalone Tag Genome README is indexed but its body could not be retrieved in this review. Do not infer its terms from MovieLens 32M or another MovieLens release.

| Dimension | MovieLens 32M | Standalone Tag Genome |
|---|---|---|
| Caching and retention | Not stated in the README. | Not stated in the accessible README content. |
| ML/AI use | No specific ML/AI clause stated. The README says, “The data set may be used for any research purposes under the following conditions”; commercial/revenue-bearing use is separately restricted below. | Not stated in the accessible README content. |
| Attribution | “The user must acknowledge the use of the data set in publications resulting from the use of the data set.” The README gives citation information; no UI attribution string is specified. | Not stated in the accessible README content. |
| Imagery rights | No image license is stated in the README. | Not stated; no image-rights clause was retrieved. |
| Commercial restrictions | “The user may not use this information for any commercial or revenue-bearing purposes without first obtaining permission from a faculty member of the GroupLens Research Project at the University of Minnesota.” | Not stated in the accessible README content. Do not assume the 32M clause applies. |
| Redistribution | “The user may redistribute the data set, including transformations, so long as it is distributed under these same license conditions.” | Not stated in the accessible README content. The separate README must be reviewed before use or redistribution. |

The MovieLens 32M redistribution wording differs from other GroupLens releases; permission is
release-specific. Do not generalize its redistribution clause to standalone Tag Genome.

## Decision inputs (D2 / D3; no decision made)

| Availability vendor | Non-commercial, single-household deployment | Commercial deployment | D2/D3 input and unresolved checks |
|---|---|---|---|
| Streaming Availability API (Movie of the Night) | Public terms allow use in consumer-facing apps; availability lookup/display is a viable candidate subject to attribution and third-party rights. | Public terms expressly include commercial products, subject to the same conditions. | Candidate for availability only, not for ranker/model training, evaluation, or improvement. Do not display its images absent separate rights. No standalone availability-data redistribution. |
| Watchmode | Public Developer plan is non-commercial, requires attribution, and says cached data should be refreshed or deleted within 30 days. | Public paid tiers state commercial use; confirm subscription terms and costs before launch. | Public plan information supports keeping it as a candidate, but ML/AI, imagery, redistribution, and exact attribution language are not stated in the reviewed public sources. Review the actual plan/account contract before relying on it. |

The published terms therefore leave both vendors as candidates for availability resolution, but
with different obligations. MotN’s explicit ML/AI prohibition is a material constraint for D3:
availability payloads must not become ranker training, evaluation, or improvement data. Neither
vendor’s image payload should be displayed until its image rights are established.

### Attribution text and UI placement to implement

These are implementation requirements based on the cited terms; where a vendor prescribes no
exact wording, the proposed credit is identified as our wording, not a vendor-mandated string.

| Source/use | Text | Placement |
|---|---|---|
| MotN availability only | `Streaming availability information is provided by Streaming Availability API by Movie of the Night.` Link the provider name to `https://www.movieofthenight.com/about/api`. | Visible adjacent to the availability results/card, in the same view. |
| MotN availability plus an image (only if separately cleared) | `Streaming availability metadata and images are provided by Streaming Availability API by Movie of the Night.` Include the same required link. | Adjacent to the displayed availability and image. |
| MotN image only (only if separately cleared) | `Images are provided by Streaming Availability API by Movie of the Night.` Include the same required link. | Adjacent to the image. |
| Watchmode | Proposed product credit: `Data provided by Watchmode` linked to Watchmode. The public source requires attribution on the free tier but does not prescribe this exact wording. | Adjacent to Watchmode-powered availability results. Verify this wording/placement against the actual plan terms. |
| TVmaze | Link the visible text `TVmaze` to the corresponding TVmaze page. The API docs permit satisfying attribution by linking back; no exact label is prescribed. | In the TV details/episode information view near the sourced data. |
| Wikipedia text | Template: `Text adapted from [article title] on Wikipedia; licensed under CC BY-SA 4.0. [Article] · [license] · [history/authors]`. Populate links and creator/notice details for the actual article. | Immediately under the reused text or in a one-click source/attribution panel attached to it. |
| Wikidata structured data | No license credit required. Optional provenance label: `Structured data: Wikidata (CC0)`. | Catalog source/provenance panel; not a legal attribution requirement. |
| IMDb / MovieLens / standalone Tag Genome | No app credit string is specified here: IMDb data is excluded from a shared product absent permission; MovieLens 32M is research-only under its stated conditions; standalone Tag Genome permissions remain not stated. | Do not display or redistribute their data in the product based on this review. Record any allowed research citation in internal evaluation documentation. |

## Human review checklist

- [ ] Confirm the pinned upstream SHAs and license paths still correspond to the projects being considered; inspect nested package licenses before copying code.
- [ ] Confirm D2/D3 based on the intended deployment and selected API plans; this document provides inputs, not the decisions.
- [ ] Ensure MotN payloads are not used to train, fine-tune, evaluate, or improve ML/AI systems.
- [ ] Confirm image rights per actual file/vendor before showing posters, backdrops, or artwork; default to text cards otherwise.
- [ ] Confirm the actual Watchmode account/plan terms, especially ML/AI, imagery, redistribution, attribution wording, and retention.
- [ ] Review TVmaze/Wikipedia ShareAlike implications for stored derived features and redistributed outputs.
- [ ] Retrieve and review the standalone Tag Genome README terms before using or redistributing that dataset.
- [ ] Verify each required attribution appears in the stated UI placement and that source links work.
