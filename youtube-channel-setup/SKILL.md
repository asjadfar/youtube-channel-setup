---
name: youtube-channel-setup
description: End-to-end YouTube channel creation and branding — Claude sets up a complete, ready-to-publish YouTube channel from a brief (Google account and country/language settings, channel name and handle, channel description, profile picture and banner with safe-area check, channel settings, made-for-kids setting, links, launch checklist with approval gate). Modeled on the live channel Bunny Sounds (https://www.youtube.com/@BunnySoundsKids — kids' learning channel, white bunny with blue bow host, six animal friends). Use when the user asks to create, set up, brand, or launch a YouTube channel, pick a channel name or handle, write a channel description, design a banner or profile picture, or prepare a channel for its first video.
---

# YouTube Channel Setup

## When to use

Use this skill when the user asks to create a YouTube channel from scratch, set up or brand a channel, pick a channel name or handle, write a channel description, make a profile picture or banner, configure channel settings (default upload settings, language, made-for-kids, links), or run a pre-launch check before the first video. The end result is a complete, branded channel that is ready to publish its first video — not a half-finished account.

Do not use it for making a video (use the youtube-shorts-automation or youtube-long-video-automation skills), for video SEO on an existing video (use youtube-video-seo), or for growing a channel that is already live, unless the user explicitly asks to adapt it.

## Who does what — Claude handles all the work end to end

Claude runs every step of the workflow below — brief, account and country/language plan, name and handle, description, branding specs and safe-area check, settings, links, launch checklist. The owner is involved only at these points:

1. **Channel decisions only the owner can make** — channel name, handle, niche and audience, country and language, channel description wording, the look of the profile picture and banner, the made-for-kids answer, and which links go on the channel. Claude drafts everything; the owner supplies the facts and approves them.
2. **Accounts, sign-ins and money** — creating the Google account, signing in to YouTube, verifying the channel (phone number), and any payment detail (for example a YouTube Premium or channel-membership setup, if ever used). These happen on the owner's own device, with the owner's own details. Claude never handles the owner's password or verification code.
3. **Approval gates** — the owner approves the channel name and handle, the description, the profile picture and banner, the settings, and the final launch checklist before anything goes live (see Step 8). Nothing is published without that approval.

Two device-bound exceptions, stated honestly so the "end to end" claim is not overstated:

- **Google account and YouTube sign-in:** Claude cannot create a Google account or sign in as the owner. The owner creates the account and signs in on their own device. Claude prepares everything else — the brief, the name and handle options, the description, the branding specs, the settings list — so the owner only has to type in what Claude prepared.
- **Branding images:** Claude writes the exact image brief (what the picture shows, the size, the safe area, the text) and checks the finished banner against the safe area with `scripts/banner_safe_area.py`. The images themselves are made by the owner or an image tool from Claude's brief. Claude never invents a finished profile picture or banner and never claims an unchecked banner is safe.

Everything else — research, name and handle options, description drafts, branding specs, settings plan, links, checklists — is Claude's work. Do not hand any of it back to the owner as homework.

## Channel facts — the live reference channel (do not invent others)

Bunny Sounds (https://www.youtube.com/@BunnySoundsKids) is the live channel this skill is modeled on. Use its real, verified facts as the reference example. Do not invent a different reference channel.

- **Channel:** Bunny Sounds, handle @BunnySoundsKids, channel ID UCwXlgPBRbPoGMkbLwTYviuw, created 13 November 2026.
- **Account and locale:** Google account owned by the channel owner, country United States, language English.
- **Handle note:** the preferred handle @BunnySounds was already taken, so the channel uses @BunnySoundsKids — a close variant that still reads clearly. This is the normal outcome when a short handle is taken; see Step 3.
- **Branding:** profile picture is a white bunny with a blue bow; banner is a 2560x1440 bunny-and-friends farm scene. The banner title text is cut off on desktop YouTube because desktop crops the banner to a thin strip — the characters still show. This is the warning in Step 5; do not repeat the mistake on a new channel.
- **Content rule:** a kids' learning channel. Every video teaches something (sounds, animals, colors, numbers, letters) — not rhymes only. The same host character and the same six friends appear in every episode (see "Character consistency" below).
- **Seller services (Fiverr gig https://www.fiverr.com/s/L34yBpA):** Basic $80, Standard $180, Premium $350. Unlimited revisions on all three packages.

## Hard limits — state them honestly, do not work around them

- **No credentials in the skill.** Never put a Google password, verification code, recovery detail, API key or secret in a skill file, in chat, or in a repo. Sign-ins and verification happen on the owner's own device.
- **Claude cannot create the Google account or the channel.** Only the owner can create a Google account, sign in to YouTube, and click "Create channel". Claude prepares everything and guides the owner step by step; it never claims it created the channel itself.
- **Approval gates are mandatory.** Nothing is published — not the name, handle, description, profile picture, banner or settings — until the owner approves the exact version. A changed name, image or description needs fresh approval.
- **Never invent channel facts.** Every name, handle, country, language, description line and link comes from the owner. If a fact is missing, ask — do not fill it in.
- **Handles are unique and first-come, first-served.** A handle that is taken is taken. Do not promise the owner a handle before it has been checked live in YouTube Studio, and do not suggest a handle that copies another channel's name in a way that could confuse viewers.
- **Made-for-kids is a real legal setting, not a style choice.** If the channel is made for children, it must be set that way. A made-for-kids channel has comments, notifications, personalized ads and some other features turned off by YouTube. Do not set a kids' channel to "not made for kids" to keep comments, and do not set an adult channel to "made for kids" to get a kids' audience.
- **Banner text outside the safe area will be cut off.** This is a YouTube layout fact, not a guess. Check every banner with `scripts/banner_safe_area.py` before the owner uploads it, and say plainly what will be cut off on desktop and on mobile.
- **Do not promise monetisation.** Monetisation (YouTube Partner Program) needs the channel to meet YouTube's current eligibility rules at the time the owner applies — subscribers, public watch hours, and following the rules. Claude states the current rules and what the channel still needs; it never guarantees approval, views, subscribers or earnings.
- **Never reuse another channel's branding.** Profile pictures, banners and character art must be the owner's own or made for the owner. Do not copy another channel's logo, mascot or banner.

## Character consistency — for kids' channels (optional, but do it when the channel is for children)

When the channel is for children, the characters are the channel. Keep them constant from the first video onwards:

1. **One host character, always the same.** Same species, same colors, same outfit, same distinguishing feature (for example Bunny Sounds: a white bunny with a blue bow). The host on the profile picture is the host in every video.
2. **The same friends, every episode.** Fix the friend list once and do not swap characters in and out. Bunny Sounds uses the same six friends in every episode: cow, lion, elephant, dog, duck, pig.
3. **One look.** Same art style, same colors, same proportions in every episode. If the style changes, viewers — and parents — stop recognizing the channel.
4. **Use the profile picture and banner as the character reference.** Every new image or video prompt starts from those two images, so the characters do not drift. If a generated image changes a character (wrong color, missing bow, extra friend), it is wrong — regenerate it, do not ship it.
5. **Record the character lock in the brief.** Write down the host, the friends, the colors and the style in `templates/channel-setup-brief.md` before the first video is made. A character that is not written down will drift.

This rule applies to kids' channels. For a non-kids' channel, skip it — but still keep the profile picture and banner consistent with the channel's look.

## Workflow

### Step 1 — Brief (decisions first, no building before this)

Collect and write down, in `templates/channel-setup-brief.md`:

1. Channel name (first choice and two backups), and who the channel is for.
2. Niche and what viewers learn from every video (for a kids' learning channel: the learning topics — sounds, animals, colors, numbers, letters — not just "rhymes").
3. Country and language. Record why they were chosen (see Step 2).
4. The Google account to use (the owner's account — write "owner's Google account", never a password or recovery detail).
5. Handle: preferred handle and two variants in case it is taken.
6. Description draft inputs: audience, what the channel teaches or does, upload rhythm (how often, which days if known).
7. Branding: profile picture idea, banner idea, colors, and — for a kids' channel — the character lock (host + friends + style).
8. Made-for-kids answer: is the channel made for children? (Yes / No / mixed — see Step 6.)
9. Links to put on the channel (website, Fiverr gig, social accounts) — only links the owner gave.
10. Anything the owner explicitly does NOT want (for example: no copied branding, no handle that misleads viewers, no monetisation promise).

Do not start Step 2 until the brief is filled in and the owner has confirmed it. A missing channel name or a missing made-for-kids answer is a blocker, not something to guess.

### Step 2 — Google account, country and language

1. **Google account:** the owner creates (or picks) the Google account on their own device and signs in to YouTube with it. One channel per account is the clean setup; a second channel on the same account is possible through YouTube's channel switcher, but do not recommend it for a brand channel the owner may later hand over or sell.
2. **Country:** set the channel country in YouTube Studio > Settings > Channel > Basic info. The country should be where the owner actually operates or where the audience is — it affects which features are available, which currency and tax forms apply later, and the AdSense country if the channel is monetised. Do not pick a country the owner has no connection to.
3. **Language:** set the channel language to the language the videos are in (for Bunny Sounds: English). This affects captions, recommendations and search. If the channel is in more than one language, pick the main one and record the others in the brief.
4. **Why this matters for monetisation later:** the YouTube Partner Program checks the channel's country, language and content together. A channel whose country, language and audience do not match looks inconsistent and can slow down review. Record the choices and the reason in the brief so a later monetisation application is consistent with them.
5. **Verification:** verify the channel with the owner's phone number (YouTube Studio > Settings > Channel > Feature eligibility). Verification unlocks longer videos, custom thumbnails and live streaming. The owner enters the code on their own device; Claude never asks for it.

### Step 3 — Channel name and handle

1. **Name:** pick a name that is short, easy to say, easy to spell, and says what the channel is. For a kids' learning channel, the name should sound friendly to a parent reading it aloud. Check the name is not already used by a big channel in the same niche — a same-name search on YouTube is the check.
2. **Handle:** the handle is the channel's unique @name. It must be unique across YouTube. Check availability in YouTube Studio > Customization > Basic info, in the handle field — YouTube tells the owner immediately whether a handle is available. Claude prepares the options; the owner checks them live.
3. **When the preferred handle is taken:** do not fight for it. Pick a close variant that still reads clearly. The proven pattern from Bunny Sounds: the preferred @BunnySounds was taken, so the channel uses @BunnySoundsKids — the same name plus one clear word that says who the channel is for. Other honest variants: add "Official", "TV", or the niche word ("Kids", "Learn", "Songs"). Do not add random numbers or underscores — they are hard to remember and hard to say out loud.
4. **Consistency:** once the handle is chosen, the channel name, handle, profile picture and banner must match everywhere — YouTube, the channel's website or Fiverr gig, and any social account that points to the channel. A different name on each place confuses viewers and splits search.
5. **Record the decision:** write the final name and handle, and the two rejected options, in the brief. If the handle changes later, every place that links to the old handle must be updated — record that as a follow-up task, not as an afterthought.

### Step 4 — Channel description

Write the description from `templates/channel-description.md`. A good description answers three questions in the first two lines (YouTube shows only the first two lines before "more"):

1. **Who is this channel for?** (For example: "for toddlers and preschoolers aged 2–5, and the parents who watch with them.")
2. **What will viewers learn or get?** (For a learning channel, name the learning topics: sounds, animals, colors, numbers, letters. Do not write "fun videos" and stop there — say what is learned.)
3. **How often do videos come out?** (For example: "New videos every Tuesday and Friday." If the rhythm is not decided yet, write "New videos every week" only if that is true — do not promise a schedule the owner cannot keep.)

Keep the description short — one paragraph plus one line of links or contact. No keyword stuffing, no copied text from another channel, no promises about views or earnings. Get the owner's approval on the exact text before it is pasted into YouTube Studio.

### Step 5 — Profile picture and banner

Work from `templates/branding-spec-sheet.md`. Give the owner the exact specs and a written image brief for each image.

1. **Profile picture — 800x800 pixels minimum, square.** It shows at tiny sizes (comments, search, subscriptions), so it must read at 98x98 pixels and smaller. One clear character or symbol, centered, high contrast, no small text. For Bunny Sounds: the white bunny with a blue bow, face centered, nothing else competing with it. Export as JPG or PNG.
2. **Banner — 2560x1440 pixels.** This is the only size to design at. It is the image YouTube crops for every screen.
3. **WARNING — desktop crops the banner to a thin strip.** On desktop, YouTube shows only a 2560x423 pixel strip from the middle of the banner. On mobile it shows a 1546x423 pixel strip from the center. On TV the whole 2560x1440 image shows. This means:
   - **Title text placed in the middle or top of a 2560x1440 banner can be cut off on desktop.** Bunny Sounds learned this live: the banner title text is cut off on desktop while the characters still show.
   - **Keep all text and logos inside the safe area: 1546x423 pixels, centered.** That is the only zone that shows on every device. Put the channel name, tagline and any logo inside it — or accept that text outside it will not be seen on desktop and mobile.
   - **Put the characters in the middle band.** Characters placed in the central 423-pixel-tall band show on desktop, tablet, mobile and TV. Characters near the top or bottom edges only show on TV.
   - **Check before uploading.** Run `scripts/banner_safe_area.py` on the finished banner image. It draws the desktop, tablet, mobile and safe-area zones over the image so the owner can see exactly what survives. If the title text falls outside the safe area, say so plainly and get the banner remade — do not upload it and hope.
4. **Consistency:** the profile picture character and the banner characters must be the same characters (see "Character consistency" above for kids' channels). The banner is also the character reference for the first video.
5. **Approval:** the owner approves both images at full size and at small size (profile picture at comment size, banner as the desktop strip) before they are uploaded. An image that only looks good at full size is not approved.

### Step 6 — Channel settings

Set these in YouTube Studio > Settings > Channel and Customization, on the owner's device, from the list Claude prepares:

1. **Basic info:** country, language, channel name, handle, description, links. Links: add only the links the owner gave (website, Fiverr gig, social accounts). Check every link opens the right page.
2. **Default upload settings:** default title pattern (if the channel uses one), default description footer (subscribe line, links), default tags (only tags that describe the channel's actual content), default category, default language, default license. These save time on every upload — set them once, correctly.
3. **Made-for-kids setting:** YouTube Studio > Settings > Channel > Advanced settings. Choose one and record the reason in the brief:
   - **"Yes, set this channel as made for kids"** — for a channel whose videos are made for children. YouTube turns off comments, notifications, personalized ads, stories and some other features. This is the correct setting for a kids' learning channel like Bunny Sounds.
   - **"No, set this channel as not made for kids"** — for a channel whose videos are not made for children.
   - **"I want to review this setting for every video"** — only when the channel genuinely mixes kids' and non-kids' videos. Do not pick this to dodge the decision.
   - Never set a kids' channel to "not made for kids" to keep comments, and never set an adult channel to "made for kids" to reach children.
4. **Feature eligibility:** confirm the channel is verified (Step 2) so custom thumbnails, longer videos and live streaming are unlocked.
5. **Branding watermark (optional):** a small subscribe watermark for videos, only if the owner wants one. It must be the channel's own mark, not another channel's.
6. **Record every setting in the brief.** A setting that is not written down will be forgotten the next time the channel is checked.

### Step 7 — Links

1. Add the links the owner approved in the brief to the channel's About / Basic info section. Typical links: the owner's website, Fiverr gig, and social accounts that belong to the same brand.
2. Check every link: it must open the right page, on mobile as well as desktop. A link to the wrong handle or a dead page is a launch blocker.
3. Keep the link list short — five or fewer. A long link list looks untidy and the later links are never clicked.
4. Do not add a link the owner did not approve, and do not link to another creator's channel without the owner's say-so.

### Step 8 — Launch checklist + approval gate

Complete `templates/launch-checklist.md` for the channel. Then stop and get the owner's approval for: the channel name and handle, the description, the profile picture and banner (checked against the safe area), the settings, and the links.

Launch only after approval. The launch steps:

1. Create the channel on the owner's device (owner signs in, clicks "Create channel", enters the approved name and handle). Claude guides each screen; the owner clicks.
2. Paste the approved description, upload the approved profile picture and banner, and apply the approved settings and links.
3. Verify the channel live: open the channel URL in a signed-out browser window and check the name, handle, description, profile picture, banner (desktop strip and mobile), and links. Check on a phone as well as a desktop — most viewers are on mobile.
4. Confirm the first video plan is ready (title, topic, and who makes it) before calling the channel launched. A channel with no first video is not launched, it is just created.
5. Return the live channel URL to the owner, with the handle, the settings record, and anything still pending.

### Step 9 — After launch (first week)

1. Check the channel daily for the first week: the banner still shows correctly, the links still work, the first video is published on the planned day.
2. Fix any wrong text, wrong link or wrong image the owner reports, and re-verify live after each fix.
3. Do not change the name, handle, description or branding without the owner's approval — a handle change breaks every link that points to the old handle.
4. Record what was delivered (channel URL, handle, description, branding files, settings, first video plan) in the launch checklist so the next channel build starts from a known state.
5. Monetisation is a later step, not a launch step. When the owner asks about it, check the channel against YouTube's current Partner Program rules (subscribers, public watch hours, policy compliance) and report honestly what is still missing — never promise approval.

## How to run one channel build

1. Fill in the brief (Step 1) and get the owner to confirm it.
2. Prepare the name and handle options (Step 3) and the description draft (Step 4); get the owner to approve both.
3. Write the branding briefs and check the finished banner with `scripts/banner_safe_area.py` (Step 5).
4. Prepare the settings and links lists (Steps 6–7).
5. Fill in `templates/launch-checklist.md` and get the owner's approval at the gate (Step 8).
6. Launch on the owner's device (Step 8), then do the first-week checks (Step 9).
