"""
data/destinations.py
Rich curated destination database — powers the recommendation engine
without any external API call.
"""

DESTINATIONS = [
    {
        "id": "kyoto",
        "name": "Kyoto",
        "country": "Japan",
        "region": "East Asia",
        "flag": "🇯🇵",
        "tagline": "Where ancient temples meet living culture",
        "overview": (
            "Kyoto was Japan's imperial capital for over a millennium and remains the country's "
            "cultural soul. Seventeen UNESCO World Heritage Sites, thousands of Shinto shrines, "
            "and living traditions of tea, noh theatre and geisha culture await the curious traveller."
        ),
        "interests": ["history", "spirituality", "food", "art", "architecture", "craft"],
        "cost_level": 3,
        "best_months": [3, 4, 5, 10, 11],
        "gem_score": 0.35,
        "best_for": ["solo", "couple", "culture", "luxury"],
        "hidden_gems": [
            {
                "name": "Fushimi Inari at dawn",
                "tip": "Arrive at 5:30 AM — the 10,000 vermillion torii gates are yours alone as mist clings to the cedar forest.",
                "type": "spiritual"
            },
            {
                "name": "Nishiki Market's pickle shops",
                "tip": "Skip the tourist stalls and duck into the family-run tsukemono (pickle) shops at the market's far western end.",
                "type": "food"
            },
            {
                "name": "Philosopher's Path side alleys",
                "tip": "The famous canal walk has tiny neighbourhood shrines and tofu restaurants in the alleys that 95% of visitors walk past.",
                "type": "exploration"
            },
        ],
        "cultural_experiences": [
            {"name": "Urasenke tea ceremony", "description": "A full 90-minute ceremonial tea practice with a certified tea master in a 400-year-old tearoom.", "authenticity": 0.95, "duration": "90 mins", "cost_level": 3},
            {"name": "Nishijin weaving workshop", "description": "Learn to weave traditional Nishijin silk on a centuries-old loom alongside local artisans.", "authenticity": 0.9, "duration": "3 hours", "cost_level": 2},
            {"name": "Morning zazen at Shokokuji", "description": "Meditate with resident Zen monks before the temple opens to tourists.", "authenticity": 0.85, "duration": "1 hour", "cost_level": 1},
        ],
        "heritage_sites": [
            {"name": "Kinkaku-ji (Golden Pavilion)", "era": "14th century", "significance": "Zen Buddhist temple covered in gold leaf"},
            {"name": "Gion District", "era": "17th century", "significance": "Preserved geisha quarter with machiya townhouses"},
            {"name": "Nijo Castle", "era": "1603", "significance": "Shogun's Kyoto residence with nightingale floors"},
        ],
        "local_events": [
            {"name": "Aoi Matsuri", "month": 5, "description": "Imperial procession of 500 people in Heian-era costume from the Imperial Palace to Shimogamo Shrine.", "type": "festival"},
            {"name": "Gion Matsuri", "month": 7, "description": "Month-long Shinto festival dating to 869 AD — one of Japan's three great festivals.", "type": "festival"},
            {"name": "Jidai Matsuri", "month": 10, "description": "Parade of 2,000 people spanning 12 centuries of Japanese history.", "type": "heritage"},
        ],
        "storytelling": {
            "dawn": "Before Kyoto wakes, the city breathes differently. A thin veil of mist settles between the cedar forests of the eastern hills and the tiled rooftops of the machiya townhouses below. At Fushimi Inari, the 10,000 vermillion torii gates ascend the mountain in silence — no tour groups, no camera clicks — just the sound of your footfall on ancient stone and the distant call of a shrike from somewhere deep in the canopy.",
            "culture": "Kyoto is a city that has spent 1,200 years perfecting the art of refinement. In the Nishijin district, master weavers sit at century-old looms threading gold silk into brocades that will eventually become a geisha's obi. In Gion, a maiko — an apprentice geisha — glides across rain-wet cobblestones, her lacquered geta clicking a rhythm that has echoed through these lanes since the Edo period. This is a culture that values depth over spectacle.",
            "food": "Kyoto cuisine, or kyo-ryori, is the quiet counterpart to Tokyo's extravagance. At dawn markets near Nishiki, vendors have already arranged pyramids of yuba (tofu skin), seasonal tsukemono pickles, and yaki-mochi rice cakes over charcoal. A kaiseki dinner — Japan's haute cuisine — unfolds across twelve courses, each one a seasonal poem served on hand-crafted ceramics, each flavour designed to invoke a feeling rather than simply satisfy hunger.",
            "hidden": "The Kyoto the guidebooks describe is real, but there is another city tucked inside it. In Uzumasa, a neighbourhood that predates the imperial era, Buddhist sculptors still work in wood-chip-dusted workshops producing temple icons using techniques unchanged since the 8th century. In the northern hills, the village of Kurama holds a fire festival every October 22nd that sees residents carrying flaming torches through narrow mountain streets — a ceremony that has run unbroken for over a thousand years.",
            "dusk": "As the lanterns flicker on in Gion and the golden temples catch the last angle of autumn light, Kyoto reveals why travellers return, often again and again, unable to fully name what they are looking for. It is not any single sight. It is something in the texture of the light, in the particular stillness of a garden arranged to mirror the mind, in the feeling that this city has been quietly, deliberately beautiful for longer than most countries have existed."
        },
        "etiquette": [
            "Remove shoes before entering temples, ryokans, and many restaurants",
            "Do not photograph geiko or maiko without permission",
            "Bow slightly when greeting — depth of bow reflects respect",
            "Do not eat or drink while walking; it is considered impolite",
            "Carry your rubbish — public bins are rare",
        ],
        "phrases": {"Hello": "Konnichiwa", "Thank you": "Arigatou gozaimasu", "Excuse me": "Sumimasen", "Delicious": "Oishii", "Beautiful": "Utsukushii"},
        "food_highlights": ["Kaiseki multi-course dining", "Yudofu (hot tofu)", "Matcha sweets at Uji", "Obanzai home cooking", "Kyoto-style ramen"],
    },

    {
        "id": "marrakech",
        "name": "Marrakech",
        "country": "Morocco",
        "region": "North Africa",
        "flag": "🇲🇦",
        "tagline": "A sensory labyrinth of spice, colour and history",
        "overview": (
            "Marrakech is a UNESCO World Heritage medina where medieval souks, aromatic spice "
            "markets, and 12th-century palaces sit within walking distance of riads converting "
            "centuries of Islamic architecture into living art. The Red City never sleeps."
        ),
        "interests": ["history", "architecture", "food", "craft", "art", "spirituality"],
        "cost_level": 2,
        "best_months": [3, 4, 10, 11],
        "gem_score": 0.4,
        "best_for": ["solo", "couple", "culture", "backpacker"],
        "hidden_gems": [
            {"name": "Mellah Jewish Quarter at dawn", "tip": "The former Jewish quarter's crumbling synagogues and ornate fountain are empty of tourists before 8 AM.", "type": "heritage"},
            {"name": "Mouassine Fountain neighbourhood", "tip": "The 16th-century neighbourhood around Mouassine Mosque has artisan workshops unchanged for 400 years.", "type": "craft"},
            {"name": "Night food stalls beyond Jemaa el-Fna", "tip": "Walk 200m behind the main square to find where locals actually eat — half the price, double the authenticity.", "type": "food"},
        ],
        "cultural_experiences": [
            {"name": "Private souk navigation with a local guide", "description": "Navigate 9,000 shops in 18 distinct craft guilds — leather tanners, spice merchants, weavers — with a medina-born guide.", "authenticity": 0.9, "duration": "4 hours", "cost_level": 2},
            {"name": "Hammam ceremony at a neighbourhood bath", "description": "Experience the traditional Moroccan hammam ritual at a locals-only bathhouse, not the tourist version.", "authenticity": 0.95, "duration": "2 hours", "cost_level": 1},
            {"name": "Cooking class in a Riad kitchen", "description": "Learn to prepare a traditional seven-vegetable couscous and bastilla with a Fassi home cook.", "authenticity": 0.85, "duration": "5 hours", "cost_level": 2},
        ],
        "heritage_sites": [
            {"name": "Bahia Palace", "era": "19th century", "significance": "Intended to be the greatest palace of its time — 8 hectares of Islamic garden and tile-work"},
            {"name": "Saadian Tombs", "era": "16th century", "significance": "Royal mausoleum sealed for 200 years, rediscovered in 1917"},
            {"name": "Koutoubia Mosque", "era": "12th century", "significance": "The oldest and largest mosque in Marrakech — its minaret influenced the Giralda in Seville"},
        ],
        "local_events": [
            {"name": "Marrakech Popular Arts Festival", "month": 7, "description": "Troubadours, acrobats, dancers and storytellers from across Morocco converge for a week of folklore.", "type": "culture"},
            {"name": "Gnawa and World Music Festival (Essaouira nearby)", "month": 6, "description": "Four days of trance music rooted in sub-Saharan African spiritual traditions.", "type": "music"},
            {"name": "Ramadan evenings in the medina", "month": 3, "description": "After iftar, the medina transforms — storytellers, musicians and families fill every square.", "type": "spiritual"},
        ],
        "storytelling": {
            "dawn": "Just after the muezzin's call dissolves into the cool morning air, the Marrakech medina begins its daily ritual. Water carriers in red fez hats fill ornate brass vessels at neighbourhood fountains. Coppersmiths fire their braziers in the Rmila quarter, and the first scent of cumin, saffron and preserved lemon drifts from windows where unseen hands have been cooking since before light.",
            "culture": "The medina is not a neighbourhood you walk through — it is one you navigate by instinct, smell and sound. Nine thousand shops arranged by guild: the tanners in their pungent vats, the woodcarvers releasing cedar oil with each mallet blow, the weavers counting threads of silk under oil lamps. Every archway opens to another courtyard, every courtyard to another century. To get lost here is not misfortune — it is the whole point.",
            "food": "Moroccan cuisine is a conversation between continents — Berber spice traditions, Andalusian refinement, sub-Saharan depth. A proper tagine, slow-cooked in a clay pot over charcoal for three hours, is an act of patience and love. Sit on a low wooden bench in a neighbourhood restaurant where the menu is whatever was bought at the souk that morning. Order the bissara (fava bean soup) with argan oil and eat with torn khobz bread.",
            "hidden": "Behind the tourist-facing face of the medina is the Marrakech that residents actually inhabit. On Friday afternoons, the Koutoubia gardens fill with Marrakchi families — children chasing each other between orange trees, grandmothers in djellabas sharing sweet mint tea, young men playing guitar. No photographs, no selfie sticks. In the Mellah, the old Jewish quarter, Moroccan Jewish families still return each year for the Mimouna festival that celebrates the end of Passover with elaborate tables of sweet pastries.",
            "dusk": "As the sun drops behind the Atlas Mountains, Jemaa el-Fna square undergoes its nightly metamorphosis. Food stalls materialise from nowhere, snakes and smoke rise together, and the storytellers — the halqa — begin to draw circles of absorbed listeners around them. The tales they tell have been passed down orally for centuries, each narrator adding their own thread. To sit at the edge of a halqa circle at dusk, even without Arabic, is to feel the pulse of an ancient living culture."
        },
        "etiquette": [
            "Dress modestly — covered shoulders and knees in the medina",
            "Haggling is expected in souks; first price is never the real price",
            "Accept mint tea when offered — refusing is impolite",
            "Ask permission before photographing people",
            "Remove shoes when entering a mosque (non-Muslims restricted to some)",
        ],
        "phrases": {"Hello": "As-salamu alaykum", "Thank you": "Shukran", "How much?": "Bshal?", "Delicious": "Bnin", "Beautiful": "Zwina"},
        "food_highlights": ["Lamb tagine with preserved lemon", "B'stilla (pigeon pie)", "Harira soup", "Msemen flatbread", "Amlou almond-argan dip"],
    },

    {
        "id": "tbilisi",
        "name": "Tbilisi",
        "country": "Georgia",
        "region": "Caucasus",
        "flag": "🇬🇪",
        "tagline": "Europe's greatest undiscovered city",
        "overview": (
            "Tbilisi is where the Silk Road met European Christendom — a 1,600-year-old city of "
            "carved wooden balconies, ancient bathhouses fed by sulphur springs, 2,000 years of "
            "winemaking history, and a street food culture that has no equivalent on earth."
        ),
        "interests": ["history", "food", "architecture", "art", "nature", "spirituality"],
        "cost_level": 1,
        "best_months": [4, 5, 6, 9, 10],
        "gem_score": 0.85,
        "best_for": ["solo", "backpacker", "culture", "couple"],
        "hidden_gems": [
            {"name": "Abanotubani sulphur bath district", "tip": "Book a private room in one of the old bathhouses for 7 USD — the same sulphur water that built this neighbourhood 1,600 years ago.", "type": "wellness"},
            {"name": "Mtatsminda funicular park at night", "tip": "Take the Soviet-era funicular up the mountain after dark — the panorama of the lit city below is one of the great views of the Caucasus.", "type": "nature"},
            {"name": "Dezerter Bazaar on Saturday morning", "tip": "The real market of Tbilisi: farmers from the Kakheti wine region sell churchkhela, sulguni cheese, and wine in plastic bottles from car boots.", "type": "food"},
        ],
        "cultural_experiences": [
            {"name": "Qvevri wine-making at a family cellar", "description": "UNESCO-listed winemaking: ferment amber wine in a 2,000-litre clay jar buried in a family's basement — a tradition unchanged for 8,000 years.", "authenticity": 0.98, "duration": "Half day", "cost_level": 1},
            {"name": "Polyphonic choral evening at a local church", "description": "Georgian polyphonic singing is among humanity's oldest musical traditions — attend an evening rehearsal at a parish church, not a tourist performance.", "authenticity": 0.95, "duration": "1.5 hours", "cost_level": 1},
            {"name": "Supra feast with a Georgian family", "description": "A Georgian feast (supra) guided by a toastmaster (tamada) — wine, khinkali dumplings, walnut sauces and toasts that last three hours.", "authenticity": 0.92, "duration": "3 hours", "cost_level": 1},
        ],
        "heritage_sites": [
            {"name": "Narikala Fortress", "era": "4th century", "significance": "Ancient citadel overlooking the city — defended Tbilisi from Persians, Arabs and Mongols"},
            {"name": "Metekhi Church", "era": "13th century", "significance": "Clifftop church above the Kura River — site of the first Georgian church founded by St. Nino in 337 AD"},
            {"name": "Old Town (Abanotubani)", "era": "5th century", "significance": "The original city built around natural sulphur springs — the wooden balconied houses are a UNESCO candidate"},
        ],
        "local_events": [
            {"name": "Tbilisoba City Festival", "month": 10, "description": "Annual city celebration of Georgian culture — wine, dance ensembles, artisan markets and open-air feasts across the old town.", "type": "culture"},
            {"name": "New Wine Festival", "month": 5, "description": "Natural winemakers from across Georgia gather in the botanical garden — 500 labels, most unavailable outside the country.", "type": "food"},
            {"name": "Rtveli harvest season", "month": 9, "description": "September brings the entire Kakheti wine region to life — families invite strangers to help harvest and then feast for days.", "type": "seasonal"},
        ],
        "storytelling": {
            "dawn": "In the Abanotubani district, the morning begins with steam. Natural sulphur springs — the same ones that caused King Vakhtang I to found a city here in the 5th century when his hunting falcon fell into hot water and emerged cooked — still feed dozens of bathhouses whose domed rooftops rise like a cluster of stone mushrooms from the valley floor. At 7 AM, elderly Georgian men in towels sit outside the bath doors, arguing about football and pouring wine from unlabelled bottles.",
            "culture": "Georgia sits at an ancient crossroads — the Silk Road passed through here, Roman legions marched through here, and every empire that ever existed between China and Rome left something behind. What emerged from this turbulent history is one of the most distinctive cultures on earth: a script unlike any other alphabet, a wine tradition 8,000 years old, a choral music tradition so complex UNESCO calls it a Masterpiece of the Oral and Intangible Heritage of Humanity, and a hospitality that borders on the aggressive.",
            "food": "A Georgian feast is a philosophical event. The tamada — the toastmaster — stands and makes a toast. Not to health, but to peace. Not to the host, but to the homeland. Not to the present, but to all ancestors who died defending the language and culture of this place. You drink after each toast. By the third course the table has more food than the table can hold: khinkali dumplings fat with broth, lobiani bean bread, badrijani walnut-stuffed aubergine, pkhali spinach balls, churchkhela walnut-and-grape-juice candy. You will eat too much. This is the intention.",
            "hidden": "Most visitors stay in the postcard-pretty old town. A few kilometres away, the Fabrika hostel complex occupies a converted Soviet sewing factory and has become the centre of Tbilisi's extraordinary creative scene — natural wine bars, a vinyl record shop, a circus school, art galleries and a cinema all operating in former factory floors. On any given Tuesday night, a Georgian jazz trio might be playing next to a table of Azerbaijani chess players while a Swedish ceramicist fires a kiln in the corner. No one organised this. It just grew.",
            "dusk": "Tbilisi at evening from the Narikala fortress is a view that rewards patience. As the light turns the Kura River copper and the old wooden balconies catch the last sun, the city below gradually fills with sound — the polyphonic harmonics of a choir rehearsing in the Metekhi church, the clink of wine glasses in the courtyard restaurants of the Abanotubani, and the distant, lovely sound of a duduk flute carried on wind from the Vake hills. This is a city that has survived everything and chosen beauty as its resistance."
        },
        "etiquette": [
            "Refusing food or wine at a Georgian table is a genuine insult",
            "Always toast before drinking — solo drinking is frowned upon",
            "Dress modestly when entering Georgian Orthodox churches; women cover heads",
            "The thumbs-up gesture means 'go to hell' — avoid it",
            "Georgians consider offering to pay for a guest to be an honour, not a burden",
        ],
        "phrases": {"Hello": "Gamarjoba", "Thank you": "Madloba", "Cheers": "Gaumarjos", "Delicious": "Gemrieli", "Beautiful": "Lamazi"},
        "food_highlights": ["Khinkali soup dumplings", "Khachapuri cheese bread", "Shkmeruli garlic chicken", "Churchkhela walnut candy", "Qvevri amber wine"],
    },

    {
        "id": "oaxaca",
        "name": "Oaxaca",
        "country": "Mexico",
        "region": "Latin America",
        "flag": "🇲🇽",
        "tagline": "Mexico's living museum of indigenous culture",
        "overview": (
            "Oaxaca is the gastronomic and cultural capital of indigenous Mexico — home to seven "
            "moles, 16 distinct indigenous ethnic groups, the world's largest Day of the Dead "
            "celebrations, and a mezcal tradition that predates the Spanish conquest."
        ),
        "interests": ["food", "history", "craft", "spirituality", "art", "nature"],
        "cost_level": 1,
        "best_months": [10, 11, 12, 1, 2, 3],
        "gem_score": 0.65,
        "best_for": ["solo", "backpacker", "culture", "couple"],
        "hidden_gems": [
            {"name": "Teotitlán del Valle carpet weavers", "tip": "Skip the city shops and go directly to the mountain village where Zapotec weavers using pre-Columbian backstrap looms invite visitors into their homes.", "type": "craft"},
            {"name": "Etla Wednesday market", "tip": "The valley market at Etla, 16 km from the city, is where Oaxacan chefs shop — chapulines (grasshoppers), memelas (corn flatbreads) and black beans in clay pots.", "type": "food"},
            {"name": "San Agustín Etla water mill", "tip": "A 16th-century Dominican convent converted to an arts centre with a working water mill and residency studios — almost no tourists.", "type": "art"},
        ],
        "cultural_experiences": [
            {"name": "Día de los Muertos altar construction", "description": "Join a local family in building their ofrenda — a multi-tiered altar of marigolds, photos, food and smoke — on November 1st.", "authenticity": 0.98, "duration": "Full day", "cost_level": 1},
            {"name": "Mezcal palenque visit with maestro mezcalero", "description": "Visit a family mezcal distillery in the Sierra Juárez and learn the 400-year-old process of roasting, crushing and fermenting agave.", "authenticity": 0.93, "duration": "4 hours", "cost_level": 1},
            {"name": "Zapotec cooking with a market abuela", "description": "Shop for ingredients in the Mercado 20 de Noviembre with a local grandmother, then cook mole negro in her home kitchen.", "authenticity": 0.96, "duration": "5 hours", "cost_level": 1},
        ],
        "heritage_sites": [
            {"name": "Monte Albán", "era": "500 BC–900 AD", "significance": "Zapotec capital and one of the first cities in Mesoamerica — 2,000 years of continuous occupation"},
            {"name": "Santo Domingo de Guzmán", "era": "16th century", "significance": "One of the most ornate baroque churches in the Americas — its golden interior contains Mixtec genealogical jewellery"},
            {"name": "Mitla", "era": "200–900 AD", "significance": "Zapotec ceremonial centre — its geometric stone mosaics are found nowhere else on earth"},
        ],
        "local_events": [
            {"name": "Día de los Muertos", "month": 11, "description": "Two days when the veil between living and dead dissolves — cemeteries fill with candlelight, marigolds and the smell of copal smoke as families celebrate their ancestors.", "type": "spiritual"},
            {"name": "Guelaguetza Festival", "month": 7, "description": "The great indigenous dance festival: representatives from all seven Oaxacan regions perform traditional dances on the hill of Monte Albán.", "type": "heritage"},
            {"name": "Noche de Rábanos (Night of Radishes)", "month": 12, "description": "December 23rd — artisans compete to carve elaborate scenes from giant radishes. A uniquely Oaxacan spectacle running since 1897.", "type": "culture"},
        ],
        "storytelling": {
            "dawn": "The morning in Oaxaca tastes of chocolate. At the Mercado 20 de Noviembre, women in huipil tunics have been grinding cacao since 4 AM on the volcanic metates that their grandmothers' grandmothers used. The chocolate is unsweetened, grainy, perfumed with cinnamon — nothing like the confection the world exported from this ingredient. Pour it over a clay cup of atole corn porridge and eat a tlayuda flatbread the size of a frisbee, charred over a wood fire and piled with black beans, asiento lard and Oaxacan string cheese.",
            "culture": "Oaxaca is a place where pre-Columbian civilisation did not end — it adapted. The Zapotec and Mixtec peoples who built the hilltop city of Monte Albán 2,500 years ago are still here, still speaking their languages, still weaving the geometric patterns their ancestors coded into stone, still burying their dead with marigolds and memory. When November arrives and the veil between the living and the dead grows thin, entire cemeteries transform into lit cities of colour and communion.",
            "food": "Oaxacan cuisine is the most complex regional cuisine in the western hemisphere. Seven moles — black, red, yellow, green, coloradito, chichilo, amarillo — each a negotiation between dozens of ingredients, each taking days to prepare. The black mole requires scorching the chillies until they are ash, then grinding them with turkey, chocolate, charred tortillas and 30 other ingredients. The result tastes like something that cannot be described — smoky, sweet, bitter, deep, old.",
            "hidden": "Beyond the handsome colonial centre, Oaxaca is a city of workshops. In the neighbourhood of Xochimilco, women weavers sit at floor looms beneath corrugated roofs, producing tapetes that sell for thousands in New York galleries. In San Bartolo Coyotepec, the distinctive black clay pottery called barro negro is shaped entirely by hand without a wheel — a technique transmitted mother to daughter for 2,000 years, recently inscribed by UNESCO. Ask at any local market and someone will take you to a family who will teach you.",
            "dusk": "On November 1st, as darkness falls over the Etla Valley and the marigold petals form orange rivers from the cemetery gates to the family plots within, something happens to a visitor that is difficult to describe to those who have not experienced it. The dead are not mourned in Oaxaca — they are welcomed back. Tamales are placed on altars. Mezcal is poured. Photographs of grandparents smile from candle-lit shrines. The air smells of copal resin, marigold and wood smoke. For one evening, mortality feels less like an ending and more like a different kind of beginning."
        },
        "etiquette": [
            "Never photograph indigenous women without explicit permission",
            "Bargaining is acceptable in markets but not in restaurants",
            "Day of the Dead celebrations are family ceremonies, not tourist performances — be respectful and unobtrusive",
            "Learn two or three words of Zapotec — the effort is deeply appreciated",
            "Never turn down a mezcal offered in friendship",
        ],
        "phrases": {"Hello": "Kwa'a bidxe (Zapotec)", "Thank you": "Dyòsi bë'zha (Zapotec)", "Cheers": "Salud", "Delicious": "Delicioso", "Beautiful": "Hermoso"},
        "food_highlights": ["Mole negro con pavo", "Tlayuda oaxaqueña", "Chapulines (toasted grasshoppers)", "Tejate corn-cacao drink", "Memelas with black beans"],
    },

    {
        "id": "hoian",
        "name": "Hội An",
        "country": "Vietnam",
        "region": "Southeast Asia",
        "flag": "🇻🇳",
        "tagline": "A lantern-lit trading port frozen in the 15th century",
        "overview": (
            "Hội An's ancient town is a UNESCO World Heritage Site — 1,100 classified heritage "
            "buildings along streets that have been unchanged since Chinese, Japanese and European "
            "merchants shared this port city in the 15th century. At night, silk lanterns transform "
            "the entire old town into a living work of art."
        ),
        "interests": ["history", "craft", "food", "art", "architecture"],
        "cost_level": 1,
        "best_months": [2, 3, 4, 5, 8, 9],
        "gem_score": 0.5,
        "best_for": ["couple", "solo", "culture", "backpacker"],
        "hidden_gems": [
            {"name": "Kim Bong carpentry village", "tip": "Cross the Thu Bon River to the village that built Hội An's heritage buildings — fourth-generation woodcarvers still produce traditional joinery in open workshops.", "type": "craft"},
            {"name": "Trà Quế vegetable village at dawn", "tip": "Arrive at sunrise to see farmers irrigating organic herb gardens using traditional river-water wheels — then cook what they grow.", "type": "nature"},
            {"name": "An Bang Beach north end", "tip": "Walk 20 minutes north from the tourist beach section to where local fishing families dry squid on the shore and sell it still warm from the fire.", "type": "food"},
        ],
        "cultural_experiences": [
            {"name": "Lantern making with a heritage family", "description": "Sit in a Trần family workshop — makers of Hội An silk lanterns for four generations — and assemble a lantern by hand using bamboo, lacquer and hand-dyed silk.", "authenticity": 0.92, "duration": "2 hours", "cost_level": 1},
            {"name": "Cao Lầu noodle lesson", "description": "Learn to make cao lầu — a noodle dish that can only be authentically made with water from a single ancient Cham well — from a cook who has never left the old town.", "authenticity": 0.96, "duration": "3 hours", "cost_level": 1},
            {"name": "Full moon lantern festival", "description": "On the 14th of each lunar month, the old town cuts electricity and lights 10,000 silk lanterns — join the procession along the riverside.", "authenticity": 0.9, "duration": "Evening", "cost_level": 1},
        ],
        "heritage_sites": [
            {"name": "Japanese Covered Bridge", "era": "1590s", "significance": "Built by the Japanese merchant community — the only covered bridge in Vietnam"},
            {"name": "Phùng Hưng Old House", "era": "1780", "significance": "Architecture combining Japanese, Chinese and Vietnamese elements — still owned by the same family after 8 generations"},
            {"name": "Assembly Hall of the Cantonese Chinese Congregation", "era": "1855", "significance": "Immaculate Cantonese temple with the most elaborate dragon ship carving in Southeast Asia"},
        ],
        "local_events": [
            {"name": "Hội An Lantern Festival", "month": 1, "description": "Monthly lunar cycle celebration — 10,000 lanterns float on the Thu Bon River on the 14th of each month.", "type": "culture"},
            {"name": "Tết Nguyên Đán (Lunar New Year)", "month": 1, "description": "The most important Vietnamese holiday — Hội An families open their ancestral homes for public prayer and flower offerings.", "type": "spiritual"},
            {"name": "Water Lantern ceremony", "month": 7, "description": "Families place lit lanterns on the river to guide the spirits of the deceased on their journey.", "type": "heritage"},
        ],
        "storytelling": {
            "dawn": "Before the tourist shops open their shutters, Hội An operates on a different clock. At 5 AM, fishing boats return to the Thu Bon River with their night catch, and the women who have waited at the dock since 4 AM begin sorting, weighing and arguing over prices. A morning market materialises beneath blue tarps, every vendor selling vegetables they grew in the garden plots that separate the old town from the rice paddies beyond. The streets steam with morning broth from pho carts that will pack up by 9 AM.",
            "culture": "Hội An was one of the great cosmopolitan ports of the medieval world. Japanese merchants built bridges, Chinese merchants built assembly halls, and the Dutch, Portuguese and later French left their architectural signatures in facades that now face each other across streets barely wide enough for a bicycle. The result is a city that absorbed influences from four continents and produced a culture entirely its own — nowhere more visible than in its cuisine, which fuses the cooking traditions of all its trading partners.",
            "food": "Cao lầu is a noodle dish that exists only in Hội An and cannot be properly reproduced anywhere else on earth — the noodles require water from a specific Cham well that has been in continuous use for 1,500 years. White Rose dumplings, another Hội An exclusive, are folded by a single family who have held the monopoly for generations. To eat here is to eat history.",
            "hidden": "At the Kim Bong carpentry village across the Thu Bon River, third and fourth generation craftsmen build traditional Vietnamese joinery without nails or adhesive, the same way their great-grandfathers built the heritage buildings that tourists photograph across the water. The village produces perhaps 20 visitors a week. In the evening, the artisans play cards under the banyan trees and accept cold Bia Huda from strangers.",
            "dusk": "On the 14th of each month, when the moon is full, the electricity in the old town is cut. Ten thousand silk lanterns glow amber, red and gold in windows, doorways and across the river's surface. Paper boats carrying candles are launched from the riverbank. Families sit in their doorways and play traditional music. No one is performing for tourists — this has happened on every full moon for four hundred years."
        },
        "etiquette": [
            "Remove shoes when entering homes, temples and many restaurants",
            "Dress modestly at religious sites — no shorts or sleeveless tops",
            "The head is sacred — never touch someone's head",
            "Use both hands when giving or receiving objects",
            "Loud bargaining is acceptable in markets; aggressive tone is not",
        ],
        "phrases": {"Hello": "Xin chào", "Thank you": "Cảm ơn", "Delicious": "Ngon lắm", "Beautiful": "Đẹp quá", "How much?": "Bao nhiêu tiền?"},
        "food_highlights": ["Cao lầu noodles", "White Rose dumplings", "Bánh mì Phượng", "Cơm gà (chicken rice)", "Black sesame sweet soup"],
    },

    {
        "id": "plovdiv",
        "name": "Plovdiv",
        "country": "Bulgaria",
        "region": "Eastern Europe",
        "flag": "🇧🇬",
        "tagline": "Europe's oldest continuously inhabited city",
        "overview": (
            "Plovdiv is Europe's oldest continuously inhabited city — older than Athens or Rome. "
            "The 2019 European Capital of Culture transformed its Roman ruins, Ottoman mosques, "
            "Bulgarian Revival houses and thriving arts scene into one of the continent's most "
            "underrated destinations."
        ),
        "interests": ["history", "architecture", "art", "food", "nature"],
        "cost_level": 1,
        "best_months": [4, 5, 6, 9, 10],
        "gem_score": 0.9,
        "best_for": ["solo", "backpacker", "culture", "couple"],
        "hidden_gems": [
            {"name": "Kapana Creative Quarter", "tip": "The former craftsmen's quarter has transformed into a labyrinth of indie coffee shops, vinyl record stores and avant-garde galleries — almost no international tourists.", "type": "art"},
            {"name": "Bachkovo Monastery", "tip": "60 km south of the city, one of the largest and oldest monasteries in the Balkans sits in a river gorge with frescoes dating to the 11th century.", "type": "spiritual"},
            {"name": "Dzhumaya Mosque at prayer time", "tip": "Built in 1364 on the site of a demolished cathedral, its prayer time on Fridays draws the city's Bulgarian Muslim community — a living piece of Ottoman heritage.", "type": "heritage"},
        ],
        "cultural_experiences": [
            {"name": "Roman Theatre sunset performance", "description": "Opera and theatre productions are staged in Plovdiv's 2nd-century Roman Theatre — sitting in 2,000-year-old stone seats watching a performance at sunset.", "authenticity": 0.8, "duration": "2 hours", "cost_level": 2},
            {"name": "Old Town fresco restoration workshop", "description": "Join a team of Bulgarian cultural heritage restorers working on National Revival period houses — mix pigments and apply authentic mineral plaster.", "authenticity": 0.9, "duration": "4 hours", "cost_level": 2},
            {"name": "Mekitsa breakfast at a grandma's kitchen", "description": "Several Old Town grandmothers open their homes for traditional Bulgarian breakfasts of fried mekitsa dough, honey and fresh sirene white cheese.", "authenticity": 0.97, "duration": "1 hour", "cost_level": 1},
        ],
        "heritage_sites": [
            {"name": "Ancient Stadium of Philippopolis", "era": "2nd century AD", "significance": "30,000-seat Roman stadium buried beneath the main square — its northern curve is still visible"},
            {"name": "Old Town (Stari Grad)", "era": "18th–19th century", "significance": "Bulgaria's finest National Revival architecture — coloured bay-windowed houses overhanging cobblestone lanes"},
            {"name": "Roman Theatre of Philippopolis", "era": "2nd century AD", "significance": "One of the best-preserved Roman theatres in the world — still in use for performances"},
        ],
        "local_events": [
            {"name": "Plovdiv International Fair", "month": 5, "description": "One of the oldest trade fairs in the Balkans — the city fills with merchants, exhibitors and an enormous street food culture.", "type": "culture"},
            {"name": "Night of Museums and Galleries", "month": 9, "description": "Annual September night when every museum, gallery and heritage house in the city opens free until midnight.", "type": "art"},
            {"name": "Opera Open", "month": 6, "description": "Full opera productions staged in the open-air Roman Theatre under summer stars.", "type": "music"},
        ],
        "storytelling": {
            "dawn": "Plovdiv sits on seven hills, and from the summit of the Nebet Tepe — where Thracians built a settlement in 4000 BC — the morning light reveals a city that has been continuously inhabited longer than any in Europe. Below: a 2nd-century Roman theatre still hosting performances. Adjacent: an Ottoman mosque built on a Byzantine church built on a Thracian temple. Around it: Bulgarian National Revival mansions with their cantilever upper floors painted the colours of summer fruit. Six thousand years of habitation compressed into a view you can see in twelve seconds.",
            "culture": "Every culture that passed through the Balkans left something in Plovdiv. The Thracians left gold treasure. The Romans left a stadium and a theatre. The Byzantines left churches. The Ottomans left mosques, a covered bazaar and the distinctive Bulgarian Muslim culture that still flourishes here. The Bulgarian National Revival movement left the painted mansion-houses of the Old Town. The Soviets left brutalist apartment blocks on the periphery. And in 2019, the European Union left Plovdiv the title of European Capital of Culture — and the city has not stopped celebrating since.",
            "food": "Bulgarian food is the cuisine that history forgot — which means it is honest, seasonal and cheap. Shkembe soup (tripe with garlic and vinegar) has been Plovdiv's hangover cure since the Ottoman period. Banitsa — filo pastry stuffed with white cheese and eggs — is pulled from ovens at 6 AM in bakeries that open before anyone else. Kavarma, the slow-cooked clay pot stew, is what you order when you want to eat something that tastes exactly as it did 200 years ago.",
            "hidden": "Kapana — the Trap — is what locals call the former craftsmen's quarter where weavers, cobblers and tailors once operated under low stone arches. Those artisans are long gone, replaced by a generation of artists, musicians and coffee-obsessives who have turned every former workshop into something unexpected. On a Tuesday afternoon in Kapana you might find a Bulgarian hip-hop concert, a Bulgarian whisky tasting, a vintage synth exhibition and the best espresso in the Balkans, all within a five-minute walk.",
            "dusk": "The Roman Theatre at sunset is one of those architectural experiences that literature is inadequate to describe. The stone seats are worn smooth by two thousand years of audiences. The stage faces west, so the backdrop to any performance is the gradual extinction of Plovdiv's skyline into darkness — first the church towers, then the mosque minarets, then the Rhodope Mountains in the distance. When the orchestra plays, the acoustics are so precise that a whisper on stage reaches the last row. The Romans built for permanence. They succeeded."
        },
        "etiquette": [
            "Bulgarians nod their heads to mean 'no' and shake their heads to mean 'yes' — the opposite of most cultures",
            "Refusing food at a Bulgarian home is considered insulting",
            "Dress conservatively in Orthodox churches and mosques",
            "Rakia (fruit brandy) is offered as a greeting — drinking a small amount is polite",
            "Punctuality is not strictly observed; arriving 15 minutes late is acceptable",
        ],
        "phrases": {"Hello": "Zdraveyte", "Thank you": "Blagodarya", "Cheers": "Nazdrave", "Delicious": "Vkusno", "Beautiful": "Krasivo"},
        "food_highlights": ["Banitsa cheese pastry", "Kavarma clay pot stew", "Tarator cold cucumber soup", "Lukanka sausage", "Rakia fruit brandy"],
    },

    {
        "id": "luangprabang",
        "name": "Luang Prabang",
        "country": "Laos",
        "region": "Southeast Asia",
        "flag": "🇱🇦",
        "tagline": "Buddhism's most serene living city",
        "overview": (
            "Luang Prabang is a UNESCO World Heritage city where Theravada Buddhist temples, "
            "French colonial architecture and the confluence of the Mekong and Nam Khan rivers "
            "create the most tranquil city in Southeast Asia. Every morning at dawn, hundreds "
            "of monks walk in silent procession to collect alms."
        ),
        "interests": ["spirituality", "nature", "history", "architecture", "food"],
        "cost_level": 1,
        "best_months": [11, 12, 1, 2, 3],
        "gem_score": 0.7,
        "best_for": ["solo", "couple", "backpacker", "culture"],
        "hidden_gems": [
            {"name": "Tad Sae waterfall in rainy season", "tip": "Most tourists visit Kuang Si. Tad Sae, accessible only by boat, has turquoise pools and zero crowds — visit August through October.", "type": "nature"},
            {"name": "Ban Xang Khong paper village", "tip": "The mulberry paper village across the Mekong still makes saa paper using techniques from the 14th century — artisans accept visitors who want to try the process.", "type": "craft"},
            {"name": "Night market back alley Lao food stalls", "tip": "Behind the tourist night market, a parallel street serves Lao food for local prices — khao jee (baguette sandwich), lap meat salad, and sticky rice by the kilo.", "type": "food"},
        ],
        "cultural_experiences": [
            {"name": "Tak Bat alms-giving ceremony", "description": "At 5:30 AM, participate in the daily procession of 200+ monks collecting alms from the faithful — witnessed respectfully, not photographed aggressively.", "authenticity": 0.95, "duration": "1 hour", "cost_level": 1},
            {"name": "Khaen music lesson with a village musician", "description": "The khaen — a bamboo mouth organ — is the sound of Laos. A village musician from Ban Phonheung teaches the instrument's 3,000-year history.", "authenticity": 0.9, "duration": "2 hours", "cost_level": 1},
            {"name": "Mekong sunset on a local pirogue", "description": "Hire a long-tail boat from a fisherman (not a tour company) and drift down the Mekong as the sun sets behind the Luang Prabang mountains.", "authenticity": 0.85, "duration": "2 hours", "cost_level": 1},
        ],
        "heritage_sites": [
            {"name": "Wat Xieng Thong", "era": "1560", "significance": "The most important temple in Laos — a sweeping roof that nearly touches the ground, glass mosaics depicting Lao cosmology"},
            {"name": "Royal Palace Museum", "era": "1904", "significance": "Former home of the Lao royal family — Franco-Lao architecture housing the kingdom's art treasures"},
            {"name": "Mount Phousi", "era": "18th century", "significance": "Sacred hill in the centre of the peninsula with a stupa visible from across the Mekong"},
        ],
        "local_events": [
            {"name": "Boun Pi Mai Lao (Lao New Year)", "month": 4, "description": "Three days of water-throwing, sandcastle-building at the temple, and the ceremonial bathing of Buddha images — the city becomes one enormous water fight.", "type": "spiritual"},
            {"name": "Boun Khao Phansa", "month": 7, "description": "Beginning of Buddhist Lent — monks begin three months of intensified practice, and the city's population observes strict religious discipline.", "type": "spiritual"},
            {"name": "Boun Suang Heua (Boat Racing Festival)", "month": 9, "description": "Dragon boat races on the Mekong between temple-sponsored teams — thousands of spectators on both riverbanks.", "type": "culture"},
        ],
        "storytelling": {
            "dawn": "At 5:30 AM in Luang Prabang, before the Mekong mist has lifted, the procession begins. From the gates of thirty temples across the peninsula, hundreds of saffron-robed monks emerge in silence, walking in single file along streets still dark and damp with night. The faithful kneel on the pavement with baskets of sticky rice and lotus flowers. The monks pause. The rice is offered. The monks walk on. This ceremony — Tak Bat — has happened every morning for five centuries and will happen tomorrow morning and the morning after.",
            "culture": "Laos is the only country in Southeast Asia that still operates predominantly on a Buddhist social calendar. The rhythm of the week, the month and the year is set by the lunar cycle and the Theravada monastic schedule. Temples are not tourist sites in Luang Prabang — they are the functional heart of the community, where novice monks study, elders gather, and the entire city's moral life is anchored. To visit Luang Prabang is to visit a place that has organised itself around spiritual practice rather than commerce.",
            "food": "Lao food is the quiet genius of Southeast Asian cuisine. Sticky rice — khao niao — is not a side dish here; it is the foundation of every meal, formed into balls with the fingers and used to scoop sauces, pick up grilled meat, or eaten alone. Laap — the national dish — is a salad of minced meat, toasted rice powder, fish sauce and green herbs that manages to be simultaneously delicate and explosive. At the night market, vendors serve a dozen different dishes from single burners, each one representing a different province's interpretation of the same ingredients.",
            "hidden": "Across the Mekong from the main peninsula, accessible by pirogue, the villages of Ban Xang Khong and Ban Phonheung exist at a pace that Luang Prabang's increasing tourism has not yet reached. In the paper village, families hang sheets of mulberry paper to dry in the sun. In the weaving village, women in coloured sarongs sit at floor looms producing the distinctive Lao sinh fabric that has been made in these houses since the 15th century. A cold Beer Lao costs 50 cents. No one is selling anything to tourists.",
            "dusk": "The confluence of the Mekong and Nam Khan rivers at sunset is one of the great natural spectacles of landlocked Laos. From the terrace of a riverside restaurant where the river fish was caught an hour earlier, you watch the sun go down over hills that have not changed since the French colonial botanists first drew them in the 19th century. A monk crosses the footbridge above the Nam Khan. Children swim in the shallows below. In this moment, the urgency that defines every other city in the world simply does not exist."
        },
        "etiquette": [
            "Never touch a monk — especially women must never make physical contact",
            "Dress modestly at temples — cover shoulders and knees, remove shoes",
            "Do not photograph Tak Bat with a flash or get too close — it is a religious ceremony, not a performance",
            "The Lao greeting (nop) — hands pressed together in prayer position — should be returned",
            "Never point your feet at a Buddha image or another person",
        ],
        "phrases": {"Hello": "Sabaidee", "Thank you": "Khob chai", "Delicious": "Sep lai", "Beautiful": "Ngam", "Cheers": "Nyo yo"},
        "food_highlights": ["Laap minced meat salad", "Or Lam Luang Prabang stew", "Khao soi Lao noodle soup", "Mok pa steamed fish", "Khao jee baguette"],
    },

    {
        "id": "porto",
        "name": "Porto",
        "country": "Portugal",
        "region": "Western Europe",
        "flag": "🇵🇹",
        "tagline": "Azulejo tiles, port wine and Atlantic soul",
        "overview": (
            "Porto is Portugal's second city and its emotional capital — a place of blue-tiled facades, "
            "dramatic riverside gorges, 2,000-year-old wine lodges and a fado tradition rooted in "
            "Atlantic longing. The Douro River runs through it like a vein of old gold."
        ),
        "interests": ["food", "architecture", "history", "music", "art"],
        "cost_level": 2,
        "best_months": [4, 5, 6, 9, 10],
        "gem_score": 0.45,
        "best_for": ["couple", "solo", "culture", "luxury"],
        "hidden_gems": [
            {"name": "Foz do Douro at low tide", "tip": "Where the Douro meets the Atlantic — a neighbourhood of faded belle époque villas and fishermen's taverns with no tourist infrastructure whatsoever.", "type": "nature"},
            {"name": "Libraria Lello on a rainy Tuesday morning", "tip": "Europe's most beautiful bookshop is swamped at weekends. Arrive at opening time on a wet Tuesday — you may have the Art Nouveau staircase to yourself.", "type": "architecture"},
            {"name": "Mercado do Bolhão upstairs balcony", "tip": "The newly restored iron market's upper floor is where Portuguese grandmothers shop for bacalhau and nobody else goes.", "type": "food"},
        ],
        "cultural_experiences": [
            {"name": "Port wine lodge harvest dinner in Vila Nova de Gaia", "description": "A September dinner in the caves of a 300-year-old port lodge, with a winemaker explaining each vintage poured from barrels stored since 1963.", "authenticity": 0.88, "duration": "4 hours", "cost_level": 3},
            {"name": "Azulejo tile workshop at a traditional atelier", "description": "Learn to transfer and glaze hand-painted tin-glazed tiles in a family workshop that has produced azulejos for Porto's facades since 1890.", "authenticity": 0.92, "duration": "3 hours", "cost_level": 2},
            {"name": "Fado performance at a neighbourhood taberna", "description": "Not the tourist performance in the Ribeira — real fado in a neighbourhood taberna in Cedofeita or Paranhos, where the singers are from the community.", "authenticity": 0.90, "duration": "Evening", "cost_level": 2},
        ],
        "heritage_sites": [
            {"name": "Livraria Lello", "era": "1906", "significance": "Art Nouveau bookshop whose staircase influenced J.K. Rowling — one of the most beautiful buildings in Europe"},
            {"name": "Igreja de São Francisco", "era": "14th century", "significance": "Gothic church with 300kg of gold leaf lining its baroque interior — called the most excessive church in Portugal"},
            {"name": "Palácio da Bolsa", "era": "19th century", "significance": "Former stock exchange with the Arab Room — a Moorish fantasy of carved plaster built by Christians who had never seen the Middle East"},
        ],
        "local_events": [
            {"name": "Festa de São João", "month": 6, "description": "June 23rd — Porto's greatest annual party: streets fill with plastic hammer-wielding revellers, grilled sardines, folk music and fireworks over the Douro.", "type": "culture"},
            {"name": "NOS Alive Music Festival", "month": 7, "description": "Portugal's premier music festival on the Atlantic coast, with international and Portuguese headliners.", "type": "music"},
            {"name": "Serralves em Festa", "month": 6, "description": "48-hour free contemporary arts marathon at the Serralves Museum — the greatest concentrated arts event in Iberia.", "type": "art"},
        ],
        "storytelling": {
            "dawn": "Porto wakes with the smell of pastel de nata and espresso. The cafés of the Cedofeita neighbourhood — old tiled rooms with marble counters and newspapers on wooden holders — fill with retired men reading the Jornal de Notícias and arguing about Benfica. The trams begin their groaning ascent of the Rua do Almada. On the Ribeira waterfront, fishermen set out the morning's catch on salt-bleached wooden tables. Everything here has the quality of continuity — you feel that this morning is not very different from any morning in the past hundred years.",
            "culture": "Porto is the city that funded the Portuguese empire — its merchants sent Vasco da Gama to India, its port wine cellars financed the colonisation of Brazil. Then the empire ended, and Porto returned to itself: stubborn, proud, Atlantic-facing, slightly melancholy in the way that all port cities facing open ocean become melancholy. That melancholy has a word in Portuguese — saudade — and it has a musical form — fado — and both are most authentically felt in Porto.",
            "food": "Bacalhau — salt cod — has 365 preparation methods in Portugal, one for every day of the year. Porto's version of francesinha (the 'little Frenchie') is a heart-attacking construction of steak, ham and sausage inside white bread, covered in melted cheese and a beer-and-tomato sauce, eaten at 1 AM after dancing. The pastel de nata from the Confeitaria Império in the Cedofeita has been produced to the same recipe since 1934 and remains inexplicably better than any other version.",
            "hidden": "The Foz neighbourhood, where the Douro finally releases itself into the Atlantic after travelling 900 km from the mountains of Spain, is Porto without the tourists. Belle époque summer villas, many empty and fading, line streets that end abruptly at granite boulders lashed by Atlantic surf. The tavernas here serve grilled limpets and local wine to retired fishermen and nobody else. On Sunday mornings, families walk the seafront promenade in a ritual unchanged for 60 years.",
            "dusk": "From the top of the Dom Luís I Bridge at golden hour, you can see the entire Douro gorge — the port wine lodges of Vila Nova de Gaia on one bank, the stacked medieval city of Porto on the other, the river between them catching the last light. Boats return from the sea. A street musician below has begun to play fado. The melody rises through the evening air with a quality that Portuguese culture invented a word for: saudade — a longing for something you cannot name, in a place you are already standing."
        },
        "etiquette": [
            "Porto considers itself deeply distinct from Lisbon — never confuse the two or call them similar",
            "Eating a pastel de nata with fork and knife marks you as a tourist; eat it with your hands",
            "Tipping is not mandatory but 10% is appreciated in restaurants",
            "Do not rush meals — a Portuguese lunch is a minimum two-hour commitment",
            "Bargaining is not acceptable in Porto's shops and restaurants",
        ],
        "phrases": {"Hello": "Olá", "Thank you": "Obrigado/a", "Cheers": "Saúde", "Delicious": "Delicioso", "Beautiful": "Bonito"},
        "food_highlights": ["Francesinha sandwich", "Bacalhau à Gomes de Sá", "Tripas à moda do Porto", "Caldo verde soup", "Pastel de nata"],
    },

    {
        "id": "cartagena",
        "name": "Cartagena",
        "country": "Colombia",
        "region": "Latin America",
        "flag": "🇨🇴",
        "tagline": "The jewel of the Spanish Main",
        "overview": (
            "Cartagena de Indias is the finest preserved Spanish colonial city in the Americas — "
            "a walled Caribbean port of bougainvillea-draped balconies, Afro-Caribbean music, "
            "Gabriel García Márquez's magic realism made architectural, and a culinary tradition "
            "that fuses three continents."
        ),
        "interests": ["history", "architecture", "food", "music", "art"],
        "cost_level": 2,
        "best_months": [12, 1, 2, 3, 4],
        "gem_score": 0.55,
        "best_for": ["couple", "solo", "luxury", "culture"],
        "hidden_gems": [
            {"name": "Getsemaní neighbourhood at dusk", "tip": "The neighbourhood that gentrification is only beginning to touch — Afro-Colombian street murals, salsa coming from open windows, and the most authentic evening food vendors in the city.", "type": "culture"},
            {"name": "Islas del Rosario in a fisherman's lancha", "tip": "Skip the tourist catamaran and hire a local fisherman's boat from the Bazurto market dock — the same islands, half the price, zero other tourists.", "type": "nature"},
            {"name": "Mercado de Bazurto at 6 AM", "tip": "The real food market: vendors arrive before dawn with fresh catch, tropical fruit pyramids and Afro-Caribbean street food that has not changed in 200 years.", "type": "food"},
        ],
        "cultural_experiences": [
            {"name": "Champeta music lesson in Getsemaní", "description": "Champeta is the Afro-Colombian rhythmic tradition that the city's elite spent 40 years trying to suppress. A community musician in Getsemaní teaches its history and dance.", "authenticity": 0.93, "duration": "2 hours", "cost_level": 1},
            {"name": "Palenque cultural visit", "description": "San Basilio de Palenque — 1 hour from Cartagena — was the first free African town in the Americas, founded by escaped slaves in 1603. The community speaks a Spanish-African Creole found nowhere else on earth.", "authenticity": 0.97, "duration": "Full day", "cost_level": 1},
            {"name": "Cartagena walled city photography walk at dawn", "description": "The golden-hour light on the 16th-century Spanish fortifications, with a local photographer who knows which angles appear in no guidebook.", "authenticity": 0.8, "duration": "3 hours", "cost_level": 2},
        ],
        "heritage_sites": [
            {"name": "Las Murallas (City Walls)", "era": "1586–1796", "significance": "11 km of Spanish colonial fortifications — the most complete in the Americas, a UNESCO World Heritage Site"},
            {"name": "Castillo San Felipe de Barajas", "era": "1657", "significance": "The largest Spanish fortress ever built in the Americas — never taken in 200 years of colonial rule"},
            {"name": "San Pedro Claver Church", "era": "1654", "significance": "Named for the Jesuit priest who spent 44 years advocating for enslaved Africans — his tomb is beneath the high altar"},
        ],
        "local_events": [
            {"name": "Hay Festival Cartagena", "month": 1, "description": "South America's premier literary festival — authors, journalists and thinkers fill the walled city for four days.", "type": "culture"},
            {"name": "Festival de Música del Caribe", "month": 3, "description": "Caribbean music festival bringing vallenato, champeta, porro and cumbia performers from across the region.", "type": "music"},
            {"name": "Fiestas de Independencia", "month": 11, "description": "A month of parades, beauty pageants and Afro-Colombian cultural performances celebrating Colombia's independence from Spain.", "type": "heritage"},
        ],
        "storytelling": {
            "dawn": "At 6 AM in Cartagena, the Bazurto market has already been operating for two hours. Women in pollera skirts carry towers of fruit on their heads with a balance that suggests they have been doing this since childhood — and their mothers before them, and their mothers' mothers. The Caribbean sea-bass was caught at midnight. The plantains came from a farm in the Montes de María hills at 3 AM. The fresh coconut rice is already cooking in blackened cauldrons. This is the city's actual metabolism, invisible to anyone who sleeps past 8.",
            "culture": "Cartagena was one of the great ports of the Spanish empire — the gateway through which Andean gold and silver flowed to Seville, and through which enslaved Africans were forced in the opposite direction. That history is written in the city's stones, its music, its food, its DNA. The Spanish built the walls and churches. The Africans built everything else, and then built a culture so vital, so rhythmically complex, so alive that it overpowered the culture that had tried to destroy it.",
            "food": "Colombian coastal food is not well-known outside Colombia, which is the rest of the world's loss. Sancocho de pescado — fish stew with yuca, plantain and ñame — is made by grandmothers across the Caribbean coast to recipes that have not been written down because they do not need to be. Arepas de choclo, sweet corn patties griddled and filled with fresh white cheese. Patacones — twice-fried plantain — with hogao tomato sauce. And coconut rice: the best rice preparation on earth, cooked in fresh coconut milk until the grains are perfumed and slightly sweet.",
            "hidden": "San Basilio de Palenque, one hour from Cartagena through the Colombian interior, is a village unlike any other in the Americas. Founded by an escaped slave named Benkos Biohó in 1603, it was the first free African settlement in the hemisphere — the first place in the New World where Africans successfully fought for and won their freedom. The community still speaks Palenquero, a Spanish-Kikongo Creole that exists nowhere else on earth. They still practice the traditional African burial rites and musical forms that their ancestors carried across the Atlantic. To be invited to a community evening here is to be in the presence of a cultural miracle.",
            "dusk": "From the fortifications of Castillo San Felipe at sunset, the entire city spreads below — the terracotta rooftops of the walled city, the Caribbean glittering to the west, the cumbia rhythm already starting in the Getsemaní neighbourhood below. The Spanish built these walls to protect their gold. What they could not protect was the city's soul, which long ago became something they would not have recognised: Afro-Caribbean, improvised, musical, magical — exactly as García Márquez described."
        },
        "etiquette": [
            "Time operates loosely in Cartagena — arriving 30 minutes late is normal",
            "Accepting a dance invitation is a sign of respect, not flirtation",
            "Always greet shop owners and taxi drivers with good morning/afternoon",
            "Never discuss Pablo Escobar or cartels unless a local raises it",
            "Cartagenans are intensely proud of their city — genuine curiosity about its history is deeply appreciated",
        ],
        "phrases": {"Hello": "Buenas", "Thank you": "Gracias", "Cheers": "Salud", "Delicious": "Delicioso", "Beautiful": "Hermosa"},
        "food_highlights": ["Sancocho de pescado", "Arepas de choclo", "Patacones with hogao", "Coconut rice", "Ceviche costeño"],
    },

    {
        "id": "chiangmai",
        "name": "Chiang Mai",
        "country": "Thailand",
        "region": "Southeast Asia",
        "flag": "🇹🇭",
        "tagline": "Three hundred temples and the spirit of Lanna",
        "overview": (
            "Chiang Mai was the capital of the independent Lanna Kingdom for 600 years and "
            "preserves a Buddhist culture entirely distinct from Bangkok. Three hundred temples, "
            "a thriving night bazaar, hill tribe communities in the surrounding mountains, and "
            "one of the world's great street food scenes make it Southeast Asia's cultural heart."
        ),
        "interests": ["spirituality", "food", "nature", "history", "craft", "adventure"],
        "cost_level": 1,
        "best_months": [11, 12, 1, 2, 3],
        "gem_score": 0.4,
        "best_for": ["solo", "backpacker", "family", "culture"],
        "hidden_gems": [
            {"name": "Doi Inthanon sunrise at hilltribe villages", "tip": "Drive to Thailand's highest peak at 4 AM to arrive for dawn — the Hmong and Karen villages on the way welcome visitors who arrive on foot, not in tour buses.", "type": "nature"},
            {"name": "Warorot Market's upper floor", "tip": "The famous fresh market's upper floor is entirely wholesale traders selling to restaurant owners — nobody else goes up there and the dried goods selection is extraordinary.", "type": "food"},
            {"name": "Wiang Kum Kam ancient ruins", "tip": "The predecessor city to Chiang Mai — flooded by the Ping River in 1400 and buried for 500 years. Recently excavated ruins with almost no visitors.", "type": "history"},
        ],
        "cultural_experiences": [
            {"name": "Dawn alms-giving at Doi Suthep temple", "description": "The golden Doi Suthep temple above the city at 5:30 AM when monks collect offerings — no tourists, mist in the teak forests, complete silence.", "authenticity": 0.9, "duration": "Morning", "cost_level": 1},
            {"name": "Traditional Lanna cooking with a market family", "description": "Learn the distinction between Bangkok Thai and Lanna Thai cooking — aromatic herbs, wild ginger, and fermented soybean paste — with a family from Chiang Mai's Wualai silver village.", "authenticity": 0.93, "duration": "4 hours", "cost_level": 1},
            {"name": "Hmong New Year in a mountain village", "description": "December Hmong New Year celebrations in the Doi Inthanon villages — traditional dress, courtship games played with fabric balls, and pine-resin torches.", "authenticity": 0.96, "duration": "Full day", "cost_level": 1},
        ],
        "heritage_sites": [
            {"name": "Wat Chedi Luang", "era": "1391", "significance": "Once the tallest structure in Lanna Kingdom — its ruined chedi still dominates the old city"},
            {"name": "Wat Phra Singh", "era": "1345", "significance": "Most important temple in the city — houses the Phra Singh Buddha, one of the most revered images in Northern Thailand"},
            {"name": "Three Kings Monument area", "era": "14th century", "significance": "The symbolic heart of Chiang Mai — statues of the three kings who founded the city in 1296"},
        ],
        "local_events": [
            {"name": "Yi Peng Lantern Festival", "month": 11, "description": "Thousands of paper lanterns are released simultaneously into the night sky over the Ping River — one of the most beautiful spectacles on earth.", "type": "spiritual"},
            {"name": "Songkran Water Festival", "month": 4, "description": "Thai New Year — three days of city-wide water fights, sand stupas at temples, and the ceremonial washing of Buddha images.", "type": "spiritual"},
            {"name": "Flower Festival", "month": 2, "description": "First weekend of February: flower floats, hill tribe costumes and the Doi Inthanon floral displays that make Chiang Mai look like a botanical garden.", "type": "culture"},
        ],
        "storytelling": {
            "dawn": "At Wat Phra Singh before the city wakes, a monk in saffron robes sweeps the courtyard with a bamboo broom. The sound — dry leaves on stone — is the only sound in the world at this hour. Three dogs sleep against the base of the chedi. A novice monk, perhaps eleven years old, carries water to the spirit house at the temple gate. This morning scene has occurred every morning for 600 years and represents, more than any guidebook photograph, what Chiang Mai actually is: a city organised around spiritual practice.",
            "culture": "Chiang Mai was never conquered by the Burmese who surrounded it, never quite absorbed by the Bangkok Thai who governed it, and never fully transformed by the backpackers and digital nomads who now fill its coffee shops. The Lanna culture — the culture of the northern mountain kingdom that ruled this valley for six centuries — persists in the temple architecture, the food, the dialect and above all in the festivals, which are celebrated with a devotion that feels entirely genuine rather than performed for visitors.",
            "food": "Northern Thai food is not southern Thai food mislabelled. Khao soi — a curry noodle soup with crispy fried noodles on top — is the dish that defines Chiang Mai and exists in its proper form only here. Sai ua sausage, packed with lemongrass, kaffir lime and galangal, cooked over charcoal. Nam prik ong, a pork and tomato relish eaten with raw vegetables and pork rinds. These are the foods that hill tribe communities brought down from the mountain villages generations ago and that now define what Thai food means at its roots.",
            "hidden": "Wiang Kum Kam is Chiang Mai's secret history. In the 13th century, King Mengrai founded his capital here in the Ping River valley — then watched it flood and moved everything 5 kilometres north to found Chiang Mai proper. The original city was buried in silt for 600 years. Excavations that began in the 1980s have uncovered dozens of chedis, temple foundations and ancient streets that almost nobody visits. On a Tuesday afternoon, you can walk through a ruined city that predates Chiang Mai itself in complete solitude.",
            "dusk": "Yi Peng, the night of the full moon in November, transforms Chiang Mai into something that does not have a parallel in the world. At the moment the moon rises above the Doi Suthep mountain, a communal silence falls, and then a thousand paper lanterns are released simultaneously from the Ping River bridge. They rise slowly, each one carrying a prayer, until they form a moving river of fire above the city, drifting north towards the mountains. For thirty minutes, the sky above Chiang Mai contains more light than the earth below it."
        },
        "etiquette": [
            "The monarchy is deeply revered — any disrespect is a criminal offence",
            "Remove shoes before entering all temples",
            "Never touch a monk — women especially must maintain physical distance",
            "The head is sacred, the feet are profane — never point feet at a person or Buddha image",
            "A smile in Thailand means many things; a forced smile means discomfort — respond gently",
        ],
        "phrases": {"Hello": "Sawadee kha/khrap", "Thank you": "Khob khun kha/khrap", "Delicious": "Aroi mak", "Beautiful": "Suay mak", "Cheers": "Chon gaew"},
        "food_highlights": ["Khao soi curry noodles", "Sai ua northern sausage", "Nam prik ong relish", "Kanom jeen noodles", "Sticky rice with mango"],
    },
]

# Quick lookup by id
DESTINATION_MAP = {d["id"]: d for d in DESTINATIONS}

# Interest → destinations lookup (for filtering)
INTEREST_INDEX: dict = {}
for _d in DESTINATIONS:
    for _i in _d["interests"]:
        INTEREST_INDEX.setdefault(_i, []).append(_d["id"])

ALL_INTERESTS = sorted(set(
    i for d in DESTINATIONS for i in d["interests"]
))
