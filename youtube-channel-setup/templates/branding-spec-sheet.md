# Branding Spec Sheet

Give this sheet to whoever makes the images. Every spec below is a YouTube requirement or a lesson from the live Bunny Sounds channel — not a preference.

## Profile picture

| Item | Spec |
|---|---|
| Size | 800 x 800 pixels minimum, square (JPG or PNG) |
| What it shows | One clear character or symbol, centered, high contrast |
| Text | No small text — text is unreadable at comment size |
| Check | Must read clearly at 98 x 98 pixels and smaller (comments, search, subscriptions) |

**Image brief (fill in for the channel):**

- Character / symbol:
- Colors:
- Background:
- What must NOT be in it:

**Live example — Bunny Sounds:** a white bunny with a blue bow, face centered, nothing else competing with it. The same bunny is the host in every video.

## Banner

| Item | Spec |
|---|---|
| Size | 2560 x 1440 pixels (the only size to design at; JPG or PNG) |
| Desktop shows | 2560 x 423 strip from the middle |
| Tablet shows | 1855 x 423 strip from the middle |
| Mobile shows | 1546 x 423 strip from the center |
| TV shows | Whole 2560 x 1440 image |
| Safe area | 1546 x 423 pixels, centered — x 507..2053, y 508..931 |

## WARNING — the banner crop

Desktop YouTube crops the banner to a thin 2560 x 423 strip. Mobile crops it to a 1546 x 423 strip from the center. **Title text placed in the middle or top of a 2560 x 1440 banner can be cut off on desktop.**

Bunny Sounds learned this live: the banner title text is cut off on desktop while the characters still show.

Rules that follow from this:

1. **All text and logos go inside the safe area (1546 x 423, centered).** That is the only zone that shows on every device.
2. **Characters go in the middle band.** Characters placed in the central 423-pixel-tall band show on desktop, tablet, mobile and TV. Characters near the top or bottom edges show on TV only.
3. **Check before uploading.** Run `scripts/banner_safe_area.py` on the finished banner — it draws the desktop, tablet, mobile and safe-area zones over the image. If the title text falls outside the safe area, say so plainly and get the banner remade. Do not upload it and hope.

## Banner image brief (fill in for the channel)

- Scene:
- Characters (same characters as the profile picture — see character lock):
- Channel name text (must sit inside the safe area):
- Tagline text (must sit inside the safe area, or leave it out):
- Colors:
- What must NOT be in it:

**Live example — Bunny Sounds:** a bunny-and-friends farm scene, 2560 x 1440, with the white bunny with a blue bow and the six friends (cow, lion, elephant, dog, duck, pig) in the middle band.

## Character lock (kids' channels)

Write this down before the first video is made. A character that is not written down will drift.

- **Host:** species, colors, outfit, distinguishing feature
- **Friends:** fixed list — same friends in every episode
- **Art style:** same style, same colors, same proportions in every episode
- **Reference images:** the profile picture and the banner — every new image or video prompt starts from these two images

If a generated image changes a character (wrong color, missing feature, extra friend), it is wrong — regenerate it, do not ship it.

## Approval checklist

- [ ] Profile picture reads clearly at 98 x 98 pixels
- [ ] Banner is exactly 2560 x 1440
- [ ] All banner text and logos sit inside the safe area (1546 x 423, centered)
- [ ] Banner checked with `scripts/banner_safe_area.py` — date: ____
- [ ] Banner characters are the same characters as the profile picture
- [ ] Owner approved both images at full size and at small size — date: ____
