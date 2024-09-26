class Star_Cinema:
    __hall_list = []

    def entry_hall(self,rows,cols,hall_no):
        Star_Cinema.__hall_list.append({rows,cols,hall_no})
class Star_Cinema:
    
    hall_list = []

    def entry_hall(self,hall):
    
        self.hall_list.append(hall)
  

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.seats = {}
        self.show_list = []

        self.entry_hall(self)


    def entry_show(self,id,movie_name,time):
        tp = (id,movie_name,time)
        self.show_list.append(tp)

        seat = [[0 for i in range(self.cols)]for i in range(self.rows)]
        self.seats[id] = seat

    
    def book_seats(self,id,seats_t):
        if id not in self.seats:
            print("This show is not exist.\n\n")
            return
        
        seats_of_id = self.seats[id]

        for r,c in seats_t:
            if r>=self.rows or c>=self.cols:
                print("This seat is not available.\n")
                continue
            

            if seats_of_id[r][c]==0:
                seats_of_id[r][c] = 1
                print(f"The seat {(r,c)} is successfully booked.\n\n")
            else:
                print(f"The seat {(r,c)} is alrady booked .\n")

        self.seats[id] = seats_of_id

    def view_show_list(self):
        for i in self.show_list:
            print('*'*50)
            print('+'*20)
            print(f"Show id is {i[0]} {'*'*20} \n")
            print(f"{'*'*10} The Movie name is {'*'*10}")
            print(f"{'*'*10} {i[1]} and Time:{i[2]} {'*'*10}")

    def view_available_seats(self,id):
        print()
        show = self.seats[id]
        for i in show :
            print(i)


hall1 = Hall(10,10,'111')
hall2 = Hall(10,10,'232')
hall1.entry_show(191,"Tufan","2.30pm")
hall2.entry_show(192,"Jawan","8.30pm")
while(True):


    print("1.View available show today.\n 2. View available seats\n 3.Book tickit \n 4.Exit\n")

    a = int(input("Enter what you want: "))

    if a==4:
        break
    elif a==1:
        print()
        hall1.view_show_list()
        print("\n\n")
        hall2.view_show_list()

    elif a==2:
        print(f"{'_'*10} Tofan's Seats {'_'*10}\n\n")
        
        hall1.view_available_seats(191)
        print()

        print(f"{'_'*10} Jawan's Seats {'_'*10}\n\n")
    
        hall2.view_available_seats(192)
        print("\n\n")
    elif a==3:
        print("which show you want to see? ")
        n = int(input("Enter show id: "))
        if n==191:
            x,y =map(int,input("Enter number of row and collumn: ").split()) 
            
            hall1.book_seats(n,[(x-1,y-1)])

        elif n==192:
            x,y = map(int,input("Enter number of row and collumn: ").split())
           
            hall2.book_seats(n,[(x-1,y-1)])
        else:print("invalid hall number men.")

            
    








            
           

    

        

# hall.book_seats(191,[(2,3),(3,3),(2,1),(4,4),(2,2)])
# hall.view_show_list()
# hall.view_available_seats(191)
# for i in hall.seats[191]:
#     print(i)
# hall1 = Hall(10,10,2)
# print(hall.show_list)
    
   

      
                                                                                                                                                                                                                   
# Phitron= Star_Cinema()
# star_cileplex = Phitron.entry_hall(5,5,1)
# modhumita  = Phitron.entry_hall(10,10,2)



