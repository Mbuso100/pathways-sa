"""Non-diagnostic discovery activity: no aptitude scores or personality labels."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Choice:
    id: str
    en: str
    zu: str
    reflection_en: str
    reflection_zu: str
    career_ids: tuple[str, ...]

CHOICES = (
    Choice("investigate", "Investigate the water system", "Hlola uhlelo lwamanzi", "Investigating a problem is one part of engineering and technical work. It does not mean you must become an engineer.", "Ukuhlola inkinga kuyingxenye yomsebenzi wobunjiniyela nowezobuchwepheshe. Lokhu akusho ukuthi kufanele ube unjiniyela.", ("engineering",)),
    Choice("listen", "Ask residents what they need", "Buza izakhamuzi ukuthi zidingani", "Listening to people matters in community work, research and service design. You can explore these fields without committing to them.", "Ukulalela abantu kubalulekile emsebenzini womphakathi, ocwaningweni nasekuklameni izinsiza. Ungahlola le mikhakha ngaphandle kokuzibophezela kuyo.", ("community",)),
    Choice("organize", "Plan how to share available water", "Hlela indlela yokwaba amanzi akhona", "Organizing resources is useful in logistics and operations. One choice cannot measure your ability or define your future.", "Ukuhlela izinsiza kuyasiza kwezokuthutha nokusebenza. Ukukhetha okukodwa akukwazi ukukala ikhono lakho noma ukunquma ikusasa lakho.", ("logistics",)),
)

CAREERS = (
    {"id":"engineering", "title_en":"Engineering and technical work", "title_zu":"Ubunjiniyela nomsebenzi wezobuchwepheshe", "summary_en":"Explore how people investigate, design and maintain systems. Entry routes differ by occupation and institution.", "summary_zu":"Hlola indlela abantu abaphenya, abaklama nabagcina ngayo izinhlelo. Izindlela zokungena ziyehluka ngomsebenzi nangesikhungo."},
    {"id":"community", "title_en":"Community services and research", "title_zu":"Izinsiza zomphakathi nocwaningo", "summary_en":"Explore listening, research and designing services around people's needs.", "summary_zu":"Hlola ukulalela, ucwaningo nokuklama izinsiza ngokwezidingo zabantu."},
    {"id":"logistics", "title_en":"Logistics and operations", "title_zu":"Ezokuthutha nokusebenza", "summary_en":"Explore planning, coordinating and improving how resources move.", "summary_zu":"Hlola ukuhlela, ukuxhumanisa nokuthuthukisa ukuhanjiswa kwezinsiza."},
)

def reflect(choice_id: str) -> dict:
    choice = next((c for c in CHOICES if c.id == choice_id), None)
    if choice is None:
        raise ValueError("Unknown choice")
    return {"choice_id":choice.id,"reflection":{"en":choice.reflection_en,"zu":choice.reflection_zu},"explore_career_ids":list(choice.career_ids),"disclaimer":"Exploration only; not an aptitude or IQ assessment."}
