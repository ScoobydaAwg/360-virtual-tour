import spacy
import re

nlp = spacy.load("en_core_web_sm")

keywords_set = {"a", "b", "c"}

principal_aliases = {
    "abrahamtmathew", "abrahamsir", "drabraham", "principalsroom", "principal","Principal Sir","Principal sir","abraham t mathew"
}

bursar_aliases = {
    "fatherjohnvarghese", "bursaroffice", "bursarachan", "fatherjohn", "bursarroom", "bursar"
}

assistant_bursar_aliases = {
    "fatherthomasmukalumpurath", "fatherthomas", "thomasachan", "assistantbursar", "assistantbursaroffice", "assistantbursarroom"
}

vice_principal_aliases = {
    "viceprincipal", "viceprincipaloffice", "viceprincipalroom", "doctorviswanatharao", "viswanatharao", "viswanatharaosir", "raosir"
}

intel_lab_aliases = {
    "intelunnatilab", "intellab", "intel", "unnati", "unnatilab"
}

visitors_lounge_aliases = {
    "visitorslounge", "visitorroom", "guestroom", "lounge", "visitors"
}

nursing_room_aliases = {
    "nursing", "nursingroom", "nurse", "nursingstation", "sickroom"
}

senatus_aliases = {
    "senatushall", "senatus", "senatusroom"
}

physics_lab_aliases = {"physicslab", "physics"}

chemistry_lab_aliases = {"chemistrylab", "chemistry"}

def extract_keywords(text):
    doc = nlp(text)

    keywords = []
    for token in doc:
        token_text_lower = token.text.lower()

        if token_text_lower in keywords_set:
            keywords.append("block_" + token.text.upper())

        if token_text_lower in principal_aliases:
            keywords.append("principal")

        if token_text_lower in bursar_aliases:
            keywords.append("bursar")

        if token_text_lower in assistant_bursar_aliases:
            keywords.append("assistantbursar")

        if token_text_lower in vice_principal_aliases:
            keywords.append("viceprincipal")

        if token_text_lower in intel_lab_aliases:
            keywords.append("intellab")

        if token_text_lower in visitors_lounge_aliases:
            keywords.append("visitorslounge")

        if token_text_lower in nursing_room_aliases:
            keywords.append("nursingroom")

        if token_text_lower in senatus_aliases:
            keywords.append("senatus")

        if token_text_lower in physics_lab_aliases:
            keywords.append("physicslab")

        if token_text_lower in chemistry_lab_aliases:
            keywords.append("chemistrylab")


    return keywords
