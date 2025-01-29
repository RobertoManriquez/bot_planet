def reciclar(residuo):

    waste = {
        "plástico": {
            "reciclar": ["botellas de agua", "envases de alimentos", "tapas"],
            "basura": ["plásticos mezclados con comida", "utensilios desechables sucios"]
        },
        "papel": {
            "reciclar": ["revistas", "hojas impresas", "cajas de cartón limpias"],
            "basura": ["papel higiénico usado", "servilletas sucias"]
        },
        "vidrio": {
            "reciclar": ["botellas de vidrio", "tarros", "frascos"],
            "basura": ["vidrio roto contaminado con químicos", "espejos rotos"]
        },
        "orgánico": {
            "reciclar": ["cáscaras de frutas", "restos de vegetales", "posos de café (compostaje)"],
            "basura": ["huesos grandes", "residuos cocinados en exceso de grasa"]
        },
        "metal": {
            "reciclar": ["latas de aluminio", "tapas de metal", "utensilios metálicos limpios"],
            "basura": ["metales oxidados o muy dañados"]
        },
        "otros": {
            "basura": ["pilas comunes", "pañales desechables", "bombillas"]
        }
    }

    residuo = residuo.lower()
    if residuo in waste:
        info = waste[residuo]
        re = " - ".join(info.get("reciclar", []))
        trash = " - ".join(info.get("basura", []))

        return(
            f"Tipo de residuo: {residuo}\n"
            f"Objetos que se pueden reciclar: {re}\n"
            f"Objetos que no se pueden reciclar: {trash}\n"
        )
    else:
        return "Lo siento, no reconozco ese tipo de residuo. Por favor intenta con otro."

print(reciclar(input()))