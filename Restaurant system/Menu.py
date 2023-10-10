class Menu:
    food ={
        'Burger': {
            "Hamburger" : 500,
            "Turkey burger" : 400,
            "Elk burger" : 300,
            "Wild salmon burger" : 600,
            "Beyond meat burger" : 500,
        },
        'Pizza': {
            "Cheese Pizza" : 500,
            "Veggie Pizza" : 400,
            "Pepperoni Pizza" : 300,
            "Meat Pizza" : 800,
            "Margherita Pizza" : 1000,
        },
        'Biryani': {
            "Hyderabadi Biryani" : 300,
            "Bombay Biryani " : 200,
            "Kalyani Biryani" : 250,
            "Dindigul Biryani" : 350,
            "Tehari Biryani" : 300,
        },
        'Drinks': {
            " Hot Coffee" : 100,
            "cool coffe " : 240,
            "soft drinks" : 50,
            "Milkshake" : 180,
            "Water" : 30,
        },
        'Fruits ': {
            "Apple" : 500,
            "Mango" : 400,
            "Egg fruit" : 300,
            "Rosehip" : 600,
            "Melonr" : 500,
        },
        'Turkish foods': {
            "Ezogelin corba": 300,
            "Saksuka ": 350,
            "Kisir": 300,
            "Mercimek kofte": 600,
            "Inegol kofte": 500,
        },
        'Middle Eastern foods': {
            "Hummus": 500,
            "Manakeesh ": 400,
            "Grilled halloumi": 300,
            "Foul meddamas": 600,
            "Falafel": 500,
        },
    }
    
    
    
    
    def __init__(self) -> None:
        pass
        
    def add_menu_item(self, item_type, name, price):
        Menu.food[item_type][name] = price
        
    def show_menu(self):
        for i in Menu.food:
            print(f"#################   {i}     ####################")
            print()
            c = 1
            for j in Menu.food[i]:
                print(f"Iteam {c}. {j} : {Menu.food[i][j]}")
                c+=1
            c = 1