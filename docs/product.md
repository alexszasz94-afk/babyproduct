# Babyproduct — ce este (din reel-ul sursă, 3 oct 2026)

Sursă: https://www.instagram.com/reel/Dd_5U5XOmRI/ (11,75 s, 9:16, 1080x1920) — copie în `research/Dd_5U5XOmRI/`.

## Produsul
Salopetă/combinezon de pluș pentru bebeluși, costum de **broască țestoasă roz**:
- material pluș/fleece roz cu model de „solzi” rotunzi roz mai închis;
- **carapace 3D umplută pe spate** (arată ca o pernă-țestoasă când stă cu spatele în sus);
- glugă = capul țestoasei, cu ochi negri brodați și „gură”; fața bebelușului iese prin glugă;
- burtă crem/bej cu **fermoar pe față**, de la gât la picioare;
- labe cu „degete” rotunjite la mâini și picioare (tălpi crem), codiță mică;
- picioare închise (tip bunting), potrivit 6–24 luni (bebeluș care stă / merge de mână).

## Structura reel-ului (de ce merge)
| Sec | Ce se vede |
|---|---|
| 0–1,5 | POV: un picior în șosetă împinge pe parchet ceva roz care pare o pernă/jucărie țestoasă |
| 1,5–3,7 | o întoarce cu piciorul → e o salopetă întinsă pe jos, cu fața în sus |
| 3,7–5,2 | într-un mall, un copil mic merge singur în costum, de la spate — pare o țestoasă vie |
| 5,2–7,8 | copilul pe o jucărie galbenă cu roți, de la spate/lateral, în mall |
| 7,8–10 | pe pat, bebeluș cu spatele în sus — arată exact ca o jucărie de pluș |
| 10–11,75 | se întoarce / apare de pe spate: fața bebelușului râzând în glugă (reveal) |

Text pe ecran tot timpul: „DON'T show this to a new MOM... 🥺🐢💚”. Audio: muzică (fără voce), volum normal.

Mecanica: **„pare o jucărie → de fapt e un bebeluș”** (reveal în 3 trepte: obiect → costum gol → copil în costum → fața). Textul e de tip „nu arăta asta…” = invitație la share/tag către o mamă.

## Ce trebuie de la Szasz
- poze clare ale produsului (față, spate, glugă, detaliu material) pentru referințe;
- ce culori/variante are (doar roz? și verde/albastru?), mărimi, preț, link magazin;
- dacă vrem bebeluș real sau doar personaje generate (regulile pentru copii în AI trebuie stabilite).

## Colecția de Crăciun „cadou în spate” (3 oct 2026)
Costume: Ren cu cadou, Turtă dulce cu cadou, Monstruleț verde cu cadou (personaj original, nu Grinch).
**Monstrulețul — DECIZIE FINALĂ (Szasz, 3 oct):** CU CĂCIULĂ DE MOȘ peste tot (bebeluși și animale). Design: blană verde lățoasă, burtă verde-deschis, bordură albă pufoasă în jurul feței, ochi încruntați pe frunte, urechiușe rotunde, căciulă de Moș roșie cu pompon alb cusută pe glugă, coada doar la spate, cadou roșu cu fundă aurie. Referințe finale: `output/refs-v2/monstrulet-*` (5 unghiuri). Variantele cu moț (`refs-v5-mot`), „tot verde” (`refs-v3-verde`) și „shaggy” (`refs-v4-shaggy`) sunt RESPINSE.
Referințe finale: `output/refs-v2/` (5 unghiuri / costum), prompturi în `prompts/refs-v2/`.

**Regula glugii (aceeași la toate):** gluga = capul personajului, umplut 3D. În față o singură deschidere ovală pentru fața bebelușului, căptușită cu sherpa crem. Fața personajului (ochi, nas/bot) e pe FRUNTE, deasupra deschiderii, orientată în față — fața bebelușului devine „gura” personajului (ca la țestoasă). Ceafa e simplă, fără față. Urechi/coarne/căciulă sus și lateral. Fața, fermoarul și burta în față; cadoul mereu în spate.

## Varianta pentru animale (3 oct 2026)
Aceleași 3 costume pentru câini (teckel) și pisici (British Shorthair). Reguli: mânecuțe scurte, lăbuțele LIBERE; pluș extra gros și pufos; gluga cu aceeași regulă (fața animalului prin deschidere, ochii personajului pe frunte); cadoul pe spate. Monstrulețul are CĂCIULA DE MOȘ. Turta dulce: doar 2 ochi pe glugă, fără obraji. Stil foto: cozy, seara, pătură tricotată crem, lampă caldă, brad. Referințe: `output/pets-v3-cozy/`.

## Stil „cât mai cute pentru mame” (3 oct 2026, cerut de Szasz)
Bebeluși rotofei 9–11 luni, obrăjori, ochi mari, râzând / întinzând mânuța / bosumflat amuzant; pui de animale (pisicuță British Shorthair, cățeluș teckel) cu ochi mari, privind în sus. Seara, lampă caldă, brad, pătură tricotată crem. Monstrulețul are căciulița de Moș. Referințe: `output/cute/`.

**Textura costumului (Szasz, 4 oct):** cât mai cozy și pufos — blană teddy/sherpa groasă, cu fir lung, umplutură ca la o salopetă de puf, siluetă plinuță, margini moi care prind lumina; bordura feței ca lâna de miel. Promptul de „pufoșare” peste o imagine bună: `prompts/broll/fluffy-edit.txt`.

**Reguli video (Szasz, 4 oct):**
- Structura: hook (se rotește) → B1 → B2 → B3. B-roll-urile se refolosesc între videouri; se schimbă hook-ul, camera, ambientul.
- B3 = mereu ca `output/broll-video/b3-ras-005.mp4`: prim-plan, pat alb luminos, bebe râde în glugă, o mână îl ciupește de obraz (se taie înainte să-i acopere gluga fața).
- B1 = acțiune imediat, fără să stea mult nemișcat la început.
- Hook-ul cu piciorul: costumul e ÎMPĂTURIT (ca o jucărie compactă cu cadoul deasupra), apoi se desface.
- Emoji-urile din text sunt mereu de iPhone (`engine/text_ig.py` folosește `assets/emoji-apple`).
- Emoji-urile se aleg după produsul nostru (🎁🎄💚😱🥺 etc.), niciodată 🐢 sau alte emoji ale concurenței (Szasz, 4 oct).
- B-roll-urile (B1 pat, B2 merge, B3 râde) rămân aceleași aproape mereu; la fiecare video nou se schimbă doar hook-ul, camera și bebelușul din hook (Szasz, 4 oct).
- Muzica: „Santa Baby” (Eartha Kitt, fișierul dat de Szasz în `assets/music/santa-baby.mp3`) peste toate videourile, de la 12,6 s (primul „Santa baby...”); sunetul generat rămâne încet dedesubt (30%). Script: `engine/muzica.sh` (4 oct).

**Realism (Szasz, 6 oct) — de ce par ale lor mai reale și ce facem:**
- Măsurat: ale lor au saturație ~20–30 (noi ~40), sunt mai puțin calde (R-B 19–37 vs. 45–52) și mai luminoase (125–148 vs. 115–121). Scene obișnuite, lumină de zi, cadru strâmb din mână, produs care arată ca o haină reală.
- Toate cadrele noi folosesc blocul `prompts/blocks/realism-ugc.txt` (casă obișnuită, fără luminițe/bokeh, lumină de zi neutră, culori mate, fleece sage-green cu cusături și scame, cadou din material mat).
- HOOK = MEREU Genjutsu (`hf_mult_motion_control`) cu clipul lor de hook ca mișcare + cadrele noastre (start + final) + referințele costumului; promptul insistă că produsul se ÎNLOCUIEȘTE complet (zero elemente de țestoasă).
- Un singur video odată, până iese bine.
- LECȚIE Genjutsu (6 oct): Genjutsu păstrează FORMA obiectului din clipul lor. Merge când forma lor seamănă cu a noastră sau nu contează (costum împăturit sub picior, bebe mic văzut din spate în mall). NU merge când se vede spatele/silueta mare a țestoasei (în picioare pe pat, la volan, mama cu costumul, bunicul): iese carapace rotundă cu fundă pictată, textură de solzi. Pentru acestea: Seedance din cadrul nostru realist + mișcarea descrisă în cuvinte, sau Genjutsu doar pe bucățile unde produsul e mic/ascuns.
- Genjutsu poate inventa scene noi dacă clipul de mișcare e dublat/are tăieturi — se verifică cadru cu cadru și se taie doar partea bună.
