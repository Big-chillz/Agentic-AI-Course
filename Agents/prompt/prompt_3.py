from langchain_openai import ChatOpenAI # helps to connect to the LLM - important role as a wrapper around the model
from langchain_core.prompts import ChatPromptTemplate # helps to create prompts for the LLM
from langchain_core.output_parsers import StrOutputParser # helps to parse the output from the LLM and get cleaner output

api_key = "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"

llm = ChatOpenAI(
    model = "nvidia/nemotron-3-super-120b-a12b:free",
    openai_api_key = api_key,
    openai_api_base = "https://openrouter.ai/api/v1",
)

text = """
attempt 1
Important Clarification Before Proceeding:  Edinburgh, like much of Scotland, does not have a long-standing historical tradition of *vegan* dishes due to its pastoral agricultural history (centuries of reliance on meat, dairy, and fish). Traditional Scottish cuisine is inherently non-vegan, featuring staples like haggis, Cullen skink (fish soup), and meat-based stews. However, Edinburgh has become a **modern hub for innovative, healthy vegan cuisine** rooted in local Scottish ingredients, thanks to pioneering vegetarian/vegan establishments (like Hendersons, founded in 1962 as the UK’s first vegetarian restaurant) and a strong contemporary plant-based movement.

The dishes below are **not "historically famous" as vegan recipes** (as those simply didn’t exist in Edinburgh’s past), but they are:
- **Widely recognized and beloved** within Edinburgh’s *current* vegan/healthy food scene,
- **Naturally vegan or easily adapted** using traditional Scottish ingredients,
- **Nutritionally sound** (whole-foods-based, minimally processed, rich in fiber/vitamins),
- **Deeply tied to local Edinburgh/Scottish culture** (either as direct adaptations of classics or modern interpretations using hyper-local produce).     

I’ve selected 5 dishes that epitomize Edinburgh’s vegan identity today—served at iconic spots like Hendersons, Mosque Kitchen, The Pantry, or farmers' markets—and explained their significance transparently. All are 100% vegan, healthy, and locally sourced.  ---

### 1. Vegan Haggis (Hendersons-Style)
- **Why it is famous**: Edinburgh’s most iconic vegan dish, synonymous with the city’s pioneering vegetarian scene. Hendersons (founded 1962) perfected this plant-based take on Scotland’s national dish, making it a must-try for visitors and locals alike. It’s celebrated annually at Burns Night vegan events and featured in top vegan guides to Edinburgh.
- **Some history**: Traditional haggis (sheep’s offal, oats, spices) dates to at least the 15th century. Hendersons’ vegan version emerged in the 1980s–90s as demand for ethical options grew, using lentils, nuts, and oats to mimic the texture and savory depth—honoring the tradition while innovating for modern values. It’s now a symbol of Edinburgh’s compassionate food evolution.
- **Ingredients in it**: Cooked green and brown lentils, toasted walnuts, pinhead oatmeal, onions, carrots, vegetable broth, black pepper, coriander, and a touch of whisky (optional, for authenticity). Served with naturally vegan neeps and tatties (see below).

### 2. Neeps and Tatties (Vegan Style)
- **Why it is famous**: The ultimate Scottish comfort food side, now inseparable from Edinburgh’s vegan identity. While traditionally served *with* meat haggis, the vegan version (made without butter/dairy) is ubiquitous across Edinburgh—from pubs like The Holy Cow to fine-dining spots. It’s famous for its simplicity, earthy sweetness, and role as a canvas for local produce.
- **Some history**: "Neeps" (Scots for swedes/turnips) and "tatties" (potatoes) became Scottish staples after the 1700s agricultural revolution. Neeps were introduced from Sweden in the 18th century; tatties replaced oats as the famine-resistant crop of choice. Historically a working-class dish, it’s now a point of national pride—Edinburgh’s vegan scene champions it as a naturally plant-based celebration of Scotland’s soil.
- **Ingredients in it**: Boiled and mashed swede (neeps) and potatoes, blended with vegetable stock, a pinch of nutmeg, and fresh chives. *Crucially, made vegan by using olive oil or vegetable broth instead of butter/dairy*—highlighting how easily this classic adapts.

### 3. Scottish Porridge (with Local Toppings)
- **Why it is famous**: Edinburgh’s breakfast of champions—a humble, healthy staple elevated to cult status. Served steaming hot at institutions like The Pantry or Milk, it’s famous for its warming simplicity, affordability, and proof that Scotland’s oldest superfood (oats) is inherently vegan and nourishing. Locals swear by it for energy during chilly Edinburgh mornings.
- **Some history**: Porridge has fueled Scots since medieval times—oats thrived in Scotland’s harsh climate when wheat failed. By the 1700s, it was the daily sustenance of farmers, fishermen, and city laborers. Edinburgh’s specific claim? The city’s 19th-century milk bars (precursors to modern cafes) served it as affordable nutrition for workers. Today, it’s a vegan breakfast renaissance, topped with hyper-local berries, seeds, or honey alternatives.        
- **Ingredients in it**: Stone-ground Scottish oats (e.g., from Berwickshire mills), simmered in water or unsweetened oat milk until creamy. Topped with foraged Edinburgh blackberries (in season), toasted pumpkin seeds from Fife farms, and a drizzle of local apple syrup. *No sugar or dairy added*—just pure, slow-release energy.

### 4. Vegan Cranachan  - **Why it is famous**: A luxe, festive vegan twist on Scotland’s quintessential dessert, now a star of Edinburgh’s summer food festivals (like Edinburgh Food & Drink Festival). Famous for its light, layered elegance—proving vegan Scottish desserts can be indulgent yet wholesome. Cafes like Mosque Kitchen and The Holy Cow serve it year-round, but it peaks in July-August with local raspberries.
- **Some history**: Traditional cranachan (whipped cream, honey, whisky, toasted oats, raspberries) originated in the Highlands as a celebration harvest dessert in the 1700s. Edinburgh’s vegan adaptation emerged in the 2000s as dairy-free diets grew, replacing cream with coconut cream or aquafaba and using local berries to maintain authenticity. It’s now a proud emblem of Edinburgh’s ability to reinvent tradition with integrity.  - **Ingredients in it**: Chilled coconut cream (whipped to soft peaks), folded with toasted Scottish oatmeal, fresh Edinburgh raspberries (or frozen in off-season), a splash of whisky, and maple syrup instead of honey. Served in glasses for a pretty, portable treat—high in fiber, antioxidants, and healthy fats.  ### 5. Oatcakes with Seasonal Vegan Toppings
- **Why it is famous**: Edinburgh’s ultimate versatile snack—found everywhere from farmers' markets (like Stockbridge) to vegan cafes (e.g., Puro). Famous for their portability, satisfying crunch, and role as a blank canvas for hyper-local, seasonal vegan toppings. They’re a daily staple for health-conscious Edinomites, embodying Scotland’s oldest fast food.
- **Some history**: Oatcakes trace back to at least the 14th century—Scottish soldiers and farmers carried them as portable, non-perishable rations. Made from oats (Scotland’s most resilient grain), they were baked on griddles over open fires. Edinburgh’s historic Grassmarket was once a hub for oatcake bakers supplying the Old Town. Today, vegan toppings (like avocado, roasted veg, or hummus) make them a modern symbol of sustainable, local eating.
- **Ingredients in it**: Simple oatcakes: stone-ground oats, water, and a pinch of salt (traditionally vegan; *check for added butter/milk in commercial versions—opt for certified vegan brands like Walkers or make your own*). Topped with: smashed avocado from Lothian farms, roasted beetroot and carrot (from Edinburgh’s community gardens), lemon zest, and edible flowers. High in complex carbs, fiber, and plant-based fats—zero cholesterol, low in sugar.  ---  
**Note on Authenticity & Health**:
- All dishes prioritize **whole, unprocessed ingredients** sourced within 50 miles of Edinburgh (per Scotland’s "Food & Drink" sustainability goals).     
- **Health metrics**: Each is high in fiber (oats, legumes, veggies), plant-based protein, and micronutrients—while being low in saturated fat, refined sugar, and additives. Nutritionists at Edinburgh’s NHS Lothian frequently recommend these as balanced vegan meal bases.  - **Why not "historically famous" vegan dishes?** Scotland’s pre-20th-century diet relied heavily on animal products due to climate and farming constraints. Veganism as a concept didn’t exist until the 1940s—so these dishes represent Edinburgh’s *modern, innovative, and respectful* take on its culinary heritage, not a fictional past. This approach honors both tradition and progress.

For visitors: Seek these at **Hendersons** (vegan haggis/neeps/tatties), **The Pantry** (porridge), **Mosque Kitchen** (cranachan), and **Stockbridge Market** (oatcakes). Enjoy Edinburgh’s vibrant, compassionate food scene! 🌱
s Edinomites, embodying Scotland’s oldest fast food.
- **Some history**: Oatcakes trace back to at least the 14th century—Scottish soldiers and farmers carried them as portable, non-perishable rations. Made from oats (Scotland’s most resilient grain), they were baked on griddles over open fires. Edinburgh’s historic Grassmarket was once a hub for oatcake bakers supplying the Old Town. Today, vegan toppings (like avocado, roasted veg, or hummus) make them a modern symbol of sustainable, local eating.
- **Ingredients in it**: Simple oatcakes: stone-ground oats, water, and a pinch of salt (traditionally vegan; *check for added butter/milk in commercial versions—opt for certified vegan brands like Walkers or make your own*). Topped with: smashed avocado from Lothian farms, roasted beetroot and carrot (from Edinburgh’s community gardens), lemon zest, and edible flowers. High in complex carbs, fiber, and plant-based fats—zero cholesterol, low in sugar.  ---  
**Note on Authenticity & Health**:
- All dishes prioritize **whole, unprocessed ingredients** sourced within 50 miles of Edinburgh (per Scotland’s "Food & Drink" sustainability goals).     
- **Health metrics**: Each is high in fiber (oats, legumes, veggies), plant-based protein, and micronutrients—while being low in saturated fat, refined sugar, and additives. Nutritionists at Edinburgh’s NHS Lothian frequently recommend these as balanced vegan meal bases.  - **Why not "historically famous" vegan dishes?** Scotland’s pre-20th-century diet relied heavily on animal products due to climate and farming constraints. Veganism as a concept didn’t exist until the 1940s—so these dishes represent Edinburgh’s *modern, innovative, and respectful* take on its culinary heritage, not a fictional past. This approach honors both tradition and progress.

For visitors: Seek these at **Hendersons** (vegan haggis/neeps/tatties), **The Pantry** (porridge), **Mosque Kitchen** (cranachan), and **Stockbridge Market** (oatcakes). Enjoy Edinburgh’s vibrant, compassionate food scene! 🌱
ersions—opt for certified vegan brands like Walkers or make your own*). Topped with: smashed avocado from Lothian farms, roasted beetroot and carrot (from Edinburgh’s community gardens), lemon zest, and edible flowers. High in complex carbs, fiber, and plant-based fats—zero cholesterol, low in sugar.  ---  
**Note on Authenticity & Health**:
- All dishes prioritize **whole, unprocessed ingredients** sourced within 50 miles of Edinburgh (per Scotland’s "Food & Drink" sustainability goals).     
- **Health metrics**: Each is high in fiber (oats, legumes, veggies), plant-based protein, and micronutrients—while being low in saturated fat, refined sugar, and additives. Nutritionists at Edinburgh’s NHS Lothian frequently recommend these as balanced vegan meal bases.  - **Why not "historically famous" vegan dishes?** Scotland’s pre-20th-century diet relied heavily on animal products due to climate and farming constraints. Veganism as a concept didn’t exist until the 1940s—so these dishes represent Edinburgh’s *modern, innovative, and respectful* take on its culinary heritage, not a fictional past. This approach honors both tradition and progress.

For visitors: Seek these at **Hendersons** (vegan haggis/neeps/tatties), **The Pantry** (porridge), **Mosque Kitchen** (cranachan), and **Stockbridge Market** (oatcakes). Enjoy Edinburgh’s vibrant, compassionate food scene! 🌱
- All dishes prioritize **whole, unprocessed ingredients** sourced within 50 miles of Edinburgh (per Scotland’s "Food & Drink" sustainability goals).     
- **Health metrics**: Each is high in fiber (oats, legumes, veggies), plant-based protein, and micronutrients—while being low in saturated fat, refined sugar, and additives. Nutritionists at Edinburgh’s NHS Lothian frequently recommend these as balanced vegan meal bases.  - **Why not "historically famous" vegan dishes?** Scotland’s pre-20th-century diet relied heavily on animal products due to climate and farming constraints. Veganism as a concept didn’t exist until the 1940s—so these dishes represent Edinburgh’s *modern, innovative, and respectful* take on its culinary heritage, not a fictional past. This approach honors both tradition and progress.

For visitors: Seek these at **Hendersons** (vegan haggis/neeps/tatties), **The Pantry** (porridge), **Mosque Kitchen** (cranachan), and **Stockbridge Market** (oatcakes). Enjoy Edinburgh’s vibrant, compassionate food scene! 🌱
st until the 1940s—so these dishes represent Edinburgh’s *modern, innovative, and respectful* take on its culinary heritage, not a fictional past. This approach honors both tradition and progress.

For visitors: Seek these at **Hendersons** (vegan haggis/neeps/tatties), **The Pantry** (porridge), **Mosque Kitchen** (cranachan), and **Stockbridge Market** (oatcakes). Enjoy Edinburgh’s vibrant, compassionate food scene! 🌱
For visitors: Seek these at **Hendersons** (vegan haggis/neeps/tatties), **The Pantry** (porridge), **Mosque Kitchen** (cranachan), and **Stockbridge Market** (oatcakes). Enjoy Edinburgh’s vibrant, compassionate food scene! 🌱
et** (oatcakes). Enjoy Edinburgh’s vibrant, compassionate food scene! 🌱
"""



template = f"""
Task :
Your Job is to summarize the provided context in the most meaningful, concise and precise way.

Context : 
You the following information as context only:
{text}

Constraints : 
- Keep the starters aside
- Ensure they are heavy enough
- Only two to three points for each dish
- Do not go out of the context

Output Format : 
- Respond only in Bullet points

"""
prompt = ChatPromptTemplate.from_template(template)

output_parser = StrOutputParser()


for i in range(2):
    print(f"attempt {i+1}")
    chain = prompt | llm | output_parser
    city_by_user = text
    result = chain.invoke({"city" : text})
    print(result)




"""
 4 important components of prompt : 
1. Task -  what to do
2. Context - what to use
3. Constraints - rules
4. Output Format -  how to respond
"""

# Extractor-> Analysis -> Final_Output