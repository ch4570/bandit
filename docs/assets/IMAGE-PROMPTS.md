# BANDIT image assets

## Final avatar background correction

The first avatar rendered an opaque checkerboard instead of transparency. The
selected final avatar has a solid parchment background and makes no alpha claim.
The character was preserved using this built-in image edit:

```text
Edit this BANDIT avatar. Replace ONLY the grey and white checkerboard around the raccoon with a completely uniform flat warm parchment background color #F4E8CE. Keep the raccoon's identity, expression, hat, pencil, red bandana, ink texture, pose and framing exactly the same. No transparency, no checkerboard, no pattern, no shadow backdrop, no border, no text. This is a square agent avatar, and the background should be a single solid cream color.
```


BANDIT is an original raccoon character created for this project. Both assets
were generated with the built-in `image_gen` tool on 2026-09-07, then saved in
this repository. The avatar uses the hero as its character reference. No external
character artwork was supplied. These are brand illustrations, not product
screenshots or evidence of user research.

- Hero: `docs/assets/bandit-hero.png`
- Skill avatar: `skills/bandit/assets/bandit-avatar.png`

## Hero prompt

```text
Use case: illustration-story / brand hero.
Create a polished wide GitHub README hero illustration for an original product-planning agent named BANDIT. Landscape banner approximately 1536 x 640, clean readable at 800px wide. An original charismatic raccoon outlaw from the American Old West stands on the right, about half-height to full body, wearing a broad dark tobacco cowboy hat with a slightly bent brim, faded rust-red bandana, weathered vest and dusty boots. Distinct raccoon facial mask, pointed ears and a striped tail. Smart narrow eyes, confident calm half-smile, not babyish, not menacing. Holds a big yellow pencil like a quick-draw tool, and a folded cream product-planning map with a few simple route marks and boxes in the other paw. A little rolled map at the belt instead of a weapon. No guns. Memorable clean silhouette with hand-inked contours and limited flat screenprint colors, subtle warm paper grain, premium editorial cartoon mascot with a hand-painted western poster sensibility. Not 3D, not a stock vector with gradients.
Composition: rich parchment cream background, ink-brown very large western slab-serif wordmark "BANDIT" on the left; directly below, smaller highly readable text "YOUR PRODUCT-PLANNING OUTLAW". Very small subtle saddle-brown line below that: "RESEARCH / DECIDE / SPEC / REVIEW / UPDATE". Balance generous blank space around the lettering, character on the right, single small desert mesa silhouette along the bottom at very low contrast, restrained burnt-orange sun disk behind the character. Color palette parchment #F4E8CE, espresso #2D211A, rust #AF402E, ochre #C99147, slate #58635C. Express capable outlaw energy and thoughtful planning, usable as an open-source software brand. No extra characters, no technology widgets, no flags, no company logos, no watermark. Exact text spelling; no other text. Entire composition comfortably inside edges with 60px margins.
```

## Avatar prompt

```text
Create a square avatar of the SAME original BANDIT raccoon character in the reference image. Preserve his exact identity, dark cowboy hat with rope band and asymmetrical brim, pointed ears, black raccoon eye mask, calm knowing expression, rust red bandana, hand-inked western print illustration style, espresso ink and warm cream fur. Head and shoulders only, prominent face, centered and readable at small icon sizes. A small visible yellow pencil beside his shoulder is welcome. No text, lettering, logos, scenery, gun, border or badge. Actual transparent background, clean outer silhouette, do not add paper or solid rectangle background. Keep hat and ears fully in frame with modest transparent padding. Output a polished 1024 by 1024 PNG-style avatar suitable for an agent skill icon.
```
