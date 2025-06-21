from app.db.database import SessionLocal
from app.models.semibot_model import Semibot
from app.models.color_semibot_model import Color

def seed():
    db = SessionLocal()
    try:
        if db.query(Semibot).first():
            print("Data already exists.")
            return

        bot = Semibot(
            name="AlphaBot",
            image="Semi_Black.png",
            description="The unique Semibot that contains all color variations."
        )
        db.add(bot)
        db.commit()
        db.refresh(bot)

        colors = [
            { "name": "Black", "image": "Semi_Black.png" },
            { "name": "Bright_Cyan", "image": "Semi_Bright_Cyan.png" },
            { "name": "Bronze_Yellow", "image": "Semi_Bronze_Yellow.png" },
            { "name": "Coral_Orange", "image": "Semi_Coral_Orange.png" },
            { "name": "Dark_Brick_Red", "image": "Semi_Dark_Brick_Red.png" },
            { "name": "Dark_Emerald", "image": "Semi_Dark_Emerald.png" },
            { "name": "Dark_Indigo", "image": "Semi_Dark_Indigo.png" },
            { "name": "Dark_Lime", "image": "Semi_Dark_Lime.png" },
            { "name": "Dark_Maroon", "image": "Semi_Dark_Maroon.png" },
            { "name": "Dark_Purple", "image": "Semi_Dark_Purple.png" },
            { "name": "Earth_Brown", "image": "Semi_Earth_Brown.png" },
            { "name": "Earth_Olive", "image": "Semi_Earth_Olive.png" },
            { "name": "Electric_Blue", "image": "Semi_Electric_Blue.png" },
            { "name": "Forest_Green", "image": "Semi_Forest_Green.png" },
            { "name": "Fresh_Green", "image": "Semi_Fresh_Green.png" },
            { "name": "Fuchsia_Rose", "image": "Semi_Fuchsia_Rose.png" },
            { "name": "Golden_Yellow", "image": "Semi_Golden_Yellow.png" },
            { "name": "Gray", "image": "Semi_Gray.png" },
            { "name": "Hot_Pink", "image": "Semi_Hot_Pink.png" },
            { "name": "Indigo_Blue", "image": "Semi_Indigo_Blue.png" },
            { "name": "Lavender_Blue", "image": "Semi_Lavender_Blue.png" },
            { "name": "Lavender_Purple", "image": "Semi_Lavender_Purple.png" },
            { "name": "Lemon_Yellow", "image": "Semi_Lemon_Yellow.png" },
            { "name": "Light_Coral", "image": "Semi_Light_Coral.png" },
            { "name": "Light_Fuchsia", "image": "Semi_Light_Fuchsia.png" },
            { "name": "Lime_Green", "image": "Semi_Lime_Green.png" },
            { "name": "Mint_Green", "image": "Semi_Mint_Green.png" },
            { "name": "Neon_Cyan", "image": "Semi_Neon_Cyan.png" },
            { "name": "Neon_Green", "image": "Semi_Neon_Green.png" },
            { "name": "Neon_Lime", "image": "Semi_Neon_Lime.png" },
            { "name": "Neon_Magenta", "image": "Semi_Neon_Magenta.png" },
            { "name": "Red", "image": "Semi_Red.png" },
            { "name": "Tan_Brown", "image": "Semi_Tan_Brown.png" },
            { "name": "Vivid_Orange", "image": "Semi_Vivid_Orange.png" },
            { "name": "Vivid_Violet", "image": "Semi_Vivid_Violet.png" },
            { "name": "White", "image": "Semi_White.png" }
        ]

        for color in colors:
            db.add(Color(name=color["name"], image=color["image"], semibot_id=bot.id))

        db.commit()
        print("Semibot and colors inserted successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error inserting seed data: {e}")
    finally:
        db.close()
