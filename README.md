# YouTube Channel Setup Skill

A Claude skill for end-to-end YouTube channel creation and branding, built from Asjad's real channel work. Claude handles all the work end to end — brief, Google account and country/language plan, channel name and handle, channel description, profile picture and banner with a safe-area check, channel settings, made-for-kids setting, links, and launch checklist — with the owner involved only for the decisions, accounts, sign-ins and approval gates. It is modeled on the live channel Bunny Sounds, a kids' learning channel created 13 November 2026.

## What it does

Takes a channel from brief to launch in one repeatable workflow:

1. **Brief** — channel name, audience, niche and learning topics, country and language, Google account, handle options, description inputs, branding ideas, made-for-kids answer, links. No building before the brief is confirmed.
2. **Google account, country and language** — which account to use, which country and language to set, and why the choices matter for monetisation eligibility later. Phone verification to unlock custom thumbnails, longer videos and live streaming.
3. **Channel name and handle** — how to pick a name, how to check handle availability live in YouTube Studio, and what to do when the preferred handle is taken (a close variant that still reads clearly — Bunny Sounds uses @BunnySoundsKids because @BunnySounds was taken).
4. **Channel description** — who the channel is for, what viewers learn, upload rhythm — with the key facts in the first two lines.
5. **Profile picture and banner** — profile picture 800x800 minimum, banner 2560x1440, and a clear warning that desktop YouTube crops the banner to a thin strip so title text outside the safe area gets cut off. A script overlays the crop zones on the banner so the owner sees exactly what survives.
6. **Channel settings** — default upload settings, language, made-for-kids setting, feature eligibility, links.
7. **Links** — website, Fiverr gig, social accounts — only the links the owner approved, every one checked live.
8. **Launch checklist + approval gate** — nothing goes live until the owner approves the exact name, handle, description, branding, settings and links.
9. **First week** — daily checks, fixes, delivery record. Monetisation is a later step, reported honestly against YouTube's current rules.

## Who does what — Claude handles all the work end to end

Claude runs every step — brief, name and handle options, description drafts, branding specs and safe-area check, settings plan, links, checklists. The owner is involved only at three points: (1) channel decisions only the owner can make (name, handle, niche and audience, country and language, description wording, branding look, made-for-kids answer, links); (2) accounts, sign-ins and money (Google account creation, YouTube sign-in, phone verification — all on the owner's own device); and (3) approval gates (name and handle, description, profile picture and banner, settings, final launch checklist). The two device-bound exceptions are the Google account / YouTube sign-in (Claude cannot create an account or sign in as the owner) and the branding images (Claude writes the brief and checks the banner; the images come from the owner or an image tool). Everything else is Claude's work — do not hand it back to the owner as homework.

## The live example channel

- **Channel:** Bunny Sounds — https://www.youtube.com/@BunnySoundsKids
- **Handle:** @BunnySoundsKids (preferred handle @BunnySounds was already taken)
- **Channel ID:** UCwXlgPBRbPoGMkbLwTYviuw
- **Created:** 13 November 2026
- **Country / language:** United States / English
- **Branding:** profile picture is a white bunny with a blue bow; banner is a 2560x1440 bunny-and-friends farm scene (note: the banner title text is cut off on desktop — the warning in Step 5 of `SKILL.md` comes from this)
- **Content rule:** a kids' learning channel — every video teaches something (sounds, animals, colors, numbers, letters), not rhymes only
- **Characters:** same white bunny with blue bow as host, same six friends in every episode (cow, lion, elephant, dog, duck, pig)
- **Built by:** Asjad Farooq, Shopify Store Designer — Fiverr gig https://www.fiverr.com/s/L34yBpA

## Service tiers (the seller's real packages)

| Tier | Price | Delivery | Revisions |
|---|---|---|---|
| Basic | $80 | 3 days | Unlimited |
| Standard | $180 | 5 days | Unlimited |
| Premium | $350 | 7 days | Unlimited |

Prices are the seller's Fiverr gig packages. Ask the owner which tier the build is before starting, and do not build a bigger scope than the tier covers without agreement.

## Files

```
youtube-channel-setup/
├── README.md                                  # this file
└── youtube-channel-setup/
    ├── SKILL.md                               # the Claude skill — the workflow itself
    ├── scripts/
    │   └── banner_safe_area.py                # overlays desktop / tablet / mobile crop zones on a 2560x1440 banner
    └── templates/
        ├── channel-setup-brief.md             # brief + settings record
        ├── channel-description.md             # channel description template
        ├── branding-spec-sheet.md             # profile picture + banner specs and image briefs
        └── launch-checklist.md                # pre-launch checklist + approval gate
```

## Setup

### 1. Get the brief first

Fill in `templates/channel-setup-brief.md` (Step 1 of `SKILL.md`) with the owner: channel name, audience, niche and learning topics, country and language, Google account, handle options, description inputs, branding ideas, made-for-kids answer, links. Do not start building until the owner confirms the brief.

### 2. The owner creates the account and the channel

Claude cannot create a Google account or sign in as the owner. The owner creates (or picks) the Google account and signs in to YouTube on their own device, then clicks "Create channel" and enters the name and handle Claude prepared. Claude guides each screen; the owner clicks. Do not paste passwords or verification codes into the skill files, into chat, or into a repo — credentials live only in the owner's secure storage.

### 3. Check the banner before uploading it

Run `scripts/banner_safe_area.py` on the finished 2560x1440 banner image. It draws the desktop, tablet, mobile and safe-area zones over the image and saves a checked copy, so the owner can see exactly what survives on each device. If the title text falls outside the safe area, get the banner remade — do not upload it and hope.

```bash
python3 youtube-channel-setup/scripts/banner_safe_area.py banner.png
```

Needs Pillow (`pip install pillow`). If Pillow is not installed the script prints the install command and still prints the zone measurements as text.

### 4. Use in Claude

Copy the `youtube-channel-setup/` folder into a Claude skills directory (for example a Claude Code skills folder, or a repo Claude is pointed at), or keep this whole repo and point Claude at `youtube-channel-setup/SKILL.md`. Then ask Claude to run the workflow, for example: "Set up a YouTube channel for my kids' learning videos using the youtube-channel-setup skill."

## Honest limits — read before using

- **No direct YouTube connection.** Claude does not have a built-in YouTube connection. Channel creation, sign-in, verification and publishing happen in the browser on the owner's device, with the owner's sign-in and approval. Never claim Claude created the channel itself.
- **No credentials in the skill.** No Google password, verification code, recovery detail, API key or secret is stored in these files. If a step needs a login or a code, the owner does it on their own device.
- **Approval gate is mandatory.** No name, handle, description, image or setting is published until the owner approves the exact final version. A changed name, image or description needs fresh approval.
- **Never invent channel facts.** Every name, handle, country, language, description line and link comes from the owner. Missing facts are asked, not guessed.
- **Handles are unique and first-come, first-served.** A handle that is taken is taken. Do not promise a handle before it has been checked live in YouTube Studio.
- **Banner text outside the safe area will be cut off.** Check every banner with `scripts/banner_safe_area.py` before the owner uploads it.
- **Made-for-kids is a real setting, not a style choice.** A kids' channel must be set as made for kids; the setting turns off comments, notifications and personalized ads. Do not set it wrongly to keep a feature.
- **Do not promise monetisation.** Monetisation needs the channel to meet YouTube's current Partner Program rules at the time the owner applies. Claude states the current rules and what is still missing; it never guarantees approval, views, subscribers or earnings.

## How to run one channel build

1. Fill in the brief in `templates/channel-setup-brief.md` and get the owner to confirm it.
2. Prepare the name and handle options and the description draft; get the owner to approve both.
3. Write the branding briefs and check the finished banner with `scripts/banner_safe_area.py`.
4. Prepare the settings and links lists.
5. Fill in `templates/launch-checklist.md` and get the owner's approval at the gate (Step 8 of `SKILL.md`).
6. Launch on the owner's device, then do the first-week checks (Step 9 of `SKILL.md`).
