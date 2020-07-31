from reportlab import *
from PIL import Image
from reportlab.pdfgen.canvas import Canvas
import pygame
from CLASSES import *
from datetime import datetime
import numpy as np
##La parte superior en y es 800
##El limite izquierdo en y es 50
##El limite derecho en y es 500
archive_csv = csv_class("services.csv","rt")
matrix_services = archive_csv.get_matrix()
box_group = pygame.sprite.Group()
buttons = []

buttons_box = pygame.sprite.Group()
buttons_services = []
show_services = False

rect_select = None
def draw_matrix(screen,y):
    global box_group, matrix, buttons
    trans = pygame.image.load("images/transparent.png")
    #Matrix of the items
    x = 0
    row = 0
    box_group.empty()
    buttons = []
    for line in matrix:
        row +=1
        colum = 0
        x = 0
        y += 30
        if row-1 == 1:
            bt_transparent = Button_(trans,trans,x,y,330,30, row-1, colum-1)
            buttons += [bt_transparent]
            
        else:
            for element in line:
                if colum == 0:
                    colum += 1
                    x += 150
                    box = text_group(x,y,330,30, element, row-1, colum-1)
                    box_group.add(box)
                    bt_transparent = Button_(trans,trans,x,y,330,30, row-1, colum-1)
                    buttons += [bt_transparent]
                else:
                    if colum == 1:
                        colum += 1
                        x += 330
                        box = text_group(x,y,90,30, element, row-1, colum-1)
                        box_group.add(box)
                    else:
                        colum += 1
                        x += 90
                        box = text_group(x,y,90,30, element, row-1, colum-1)
                        box_group.add(box)

def draw_matrix_services(screen, y):
    global matrix_services, buttons_services, buttons_box
    trans = pygame.image.load("images/transparent.png")
    #Matrix of the items
    row = 0
    y = y + 30
    colum = 0
    x = 150
    buttons_services = []
    buttons_box.empty()
    for line in matrix_services:
        txt = ""
        for element in line:
            txt += element
        bt_transparent = Button_(trans,trans,x,y,330,30, row, colum)
        buttons_services += [bt_transparent]
        box = text_group(x,y,330,30, txt, row, colum)
        buttons_box.add(box)
        txt = " "
        y += 30
        row += 1
        colum += 1
            


def eliminate_row_matrix(screen, B_y):
    global matrix
    m = []
    for i in range(len(matrix)-1):
        m += [matrix[i]]
    matrix = m
    draw_matrix(screen,B_y)
        
def add_row_matrix(screen, B_y):
    global matrix
    matrix += [["","","",""]]
    draw_matrix(screen,B_y)

def create_pdf():
    pass


def make_invoice_window():
    global box_group, window_c,buttons, show_services,matrix_services, buttons_services, buttons_box,matrix, rect_select
    #Settings of the screen
    pygame.init()
    weight, height = 952,768
    screen = pygame.display.set_mode((weight,height))
    scroll = 10
    scroll_ = 30
    #List of the invoice numers
    archive_csv = csv_class("invoice num.csv","rt")
    matrix_csv = archive_csv.get_matrix()
    inv_number = 1
    if matrix_csv[0] != []:
        for row in matrix_csv:
            for num in row:
                inv_number = int(num) + 1
    matrix_csv[0] += [str(inv_number)]
    print(matrix_csv)
    inv_number = str(inv_number)
    
    #Text input
    d_y = 350
    due_input = text_box(645,d_y,140,25, "")
    n_y = 400
    note_input = text_box(150,n_y,600,30, "[Add a note or instruction for your customer]")
    

    #Time
    now = datetime.now()
    now.date()


    #Caption
    pygame.display.set_caption("Make Invoice")

    #Set initial clock
    clock = pygame.time.Clock()

    #Font
    font = pygame.font.Font("times.ttf", 20)
    font_n = pygame.font.Font("timesbd.ttf", 20)
    
    #Images of the screen
    background = pygame.image.load("images/background.png")
    logo = pygame.image.load("Logo.png")
    check = pygame.image.load("images/check.png")
    check_1 = pygame.image.load("images/check_1.png")

    arrow_up = pygame.image.load("images/arrow_up.png")
    arrow_u = pygame.image.load("images/arrow_u.png")

    arrow_down = pygame.image.load("images/arrow_down.png")
    arrow_d = pygame.image.load("images/arrow_d.png")

    more = pygame.image.load("images/more.png")
    more_b = pygame.image.load("images/more_b.png")

    less = pygame.image.load("images/less.png")
    less_b = pygame.image.load("images/less_b.png")

    equal = pygame.image.load("images/equal.png")
    equal_b = pygame.image.load("images/equal_b.png")
    
    #Create the buttons and cursor
    cursor = Cursor()
    bt_check = Button(check,check_1,470,700,60,60)
    bt_up = Button(arrow_up,arrow_u,900,0,40,40)
    bt_down = Button(arrow_down,arrow_d,900,720,40,40)
    
    
    
    #permanent text
    Inv_d = "Invoice For"
    Inv_d = font_n.render(Inv_d, True, (0, 0, 0))

    C_name = "[Customer Name]"
    C_name = font.render(C_name, True, (0, 0, 0))

    C_email = "[Customer Email]"
    C_email = font.render(C_email, True, (0, 0, 0))

    Inv_n = "Invoice Number: " + inv_number
    Inv_n = font_n.render(Inv_n, True, (0, 0, 0))

    S_date = "Sent: " + str(now.date())
    S_date = font.render(S_date, True, (0, 0, 0))

    D_date = "Due: "
    D_date = font.render(D_date, True, (0, 0, 0))

    Sub = "Subtotal: "
    Sub = font.render(Sub, True, (0, 0, 0))

    Tax = "Tax: "
    Tax = font.render(Tax, True, (0, 0, 0))

    Total = "Total: "
    Total = font.render(Total, True, (0, 0, 0))
    
    #Position in y of the blits
    Inv_y = 300
    C_y = 325
    E_y = 350
    L_y = 50
    B_y = 425
    M_y = 600
    S_y = 575
    T_y = 600
    To_y = 625
    sub_input = text_box(660,S_y,90,25, "")
    tax_input = text_box(660,T_y,90,25, "")
    total_input = text_box(660,T_y,90,25, "")
    #Draw the matrix
    if not show_services:
        buttons_box.empty()
        draw_matrix(screen, B_y)
    #While of the loop
    exit_ = False
    while exit_ != True:
        #pygame.display.update()
        #Buttons dynamics
        bt_more = Button(more,more_b,150,M_y,60,60)
        bt_less = Button(less,less_b,205,M_y,60,60)
        bt_equal = Button(equal,equal_b,265,M_y+5,50,50)
        
        clock.tick(60)
        cursor.update()
        screen.blit(pygame.transform.scale(background,(weight,height)),(0,0))
        screen.blit(pygame.transform.scale(logo,(400,200)),(250,L_y))
        #Update the text box
        due_input.update(screen,cursor, True, d_y)
        note_input.update(screen,cursor, False,n_y)
        sub_input.update(screen,cursor,False,S_y)
        tax_input.update(screen,cursor,False,T_y)
        total_input.update(screen,cursor,False,To_y)
                        
        if not show_services:
            box_group.update(screen, cursor, False, None)
            buttons_box.empty()
            buttons_services = []
            for button in buttons:
                button.update(screen, cursor)
        if show_services:
            box_group.empty()
            buttons = []
            buttons_box.update(screen, cursor, False, None)
            for button in buttons_services:
                button.update(screen, cursor)
        #Blit the text
        screen.blit(Inv_d,(150,Inv_y))
        screen.blit(C_name,(150,C_y))
        screen.blit(C_email,(150,E_y))

        screen.blit(Inv_n,(600,Inv_y))
        screen.blit(S_date,(600,C_y))
        screen.blit(D_date,(600,E_y))

        screen.blit(Sub,(585,S_y))
        screen.blit(Tax,(622,T_y))
        screen.blit(Total,(610,To_y))
        
        #Update Buttons
        bt_check.update(screen, cursor)
        bt_down.update(screen,cursor)
        bt_up.update(screen,cursor)
        bt_more.update(screen,cursor)
        bt_less.update(screen,cursor)
        bt_equal.update(screen, cursor)

        #Read the changes in the matrix
        cont = 0
        sub_total = 0
        for think in matrix:
            if cont > 1:
                if think[1] != " " and think[1] != "":
                    think[3] = str(int(think[1])*int(think[2]))
                    
                if think[3] != " " and think[3] != "":
                    sub_total += int(think[3])
                    
                
            else:
                cont += 1
            
                
        #Update Display
        pygame.display.update()
        for event in pygame.event.get():
            #Update the text of the box
            due_input.text_update(event)
            note_input.text_update(event)
            sub_input.text_update(event)
            tax_input.text_update(event)
            if not show_services:
                box_group.update(screen, cursor, False, event)
                
            if show_services:
                buttons_box.update(screen, cursor, False, event)
                
            if event.type == pygame.QUIT:
                #Exit
                exit_ = True
                pygame.quit()
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not show_services:
                    for button in buttons:
                        if cursor.colliderect(button.rect):
                            print("Push Button")
                            rect_select = button.get_pos()
                            show_services = True
                            draw_matrix_services(screen, B_y)
                if show_services:
                    for button in buttons_services:
                        if cursor.colliderect(button.rect):
                            rect = button.get_pos()
                            matrix[rect_select[0]][0] = matrix_services[rect[0]][0]
                            matrix[rect_select[0]][2] = matrix_services[rect[0]][1]
                            show_services = False
                            draw_matrix(screen, B_y)
                            rect_select = None
                if cursor.colliderect(bt_check.rect):
                    print("Push Check")
                if cursor.colliderect(bt_down.rect):
                    d_y += scroll
                    n_y += scroll
                    Inv_y += scroll
                    C_y += scroll
                    E_y += scroll
                    L_y += scroll
                    B_y += scroll
                    M_y += scroll
                    S_y += scroll
                    T_y += scroll
                    To_y += scroll
                    if not show_services:
                        draw_matrix(screen, B_y)
                    if show_services:
                        draw_matrix_services(screen, B_y)
                if cursor.colliderect(bt_up.rect):
                    d_y -= scroll
                    n_y -= scroll
                    Inv_y -= scroll
                    C_y -= scroll
                    E_y -= scroll
                    L_y -= scroll
                    B_y -= scroll
                    M_y -= scroll
                    S_y -= scroll
                    T_y -= scroll
                    To_y -= scroll
                    if not show_services:
                        draw_matrix(screen, B_y)
                    if show_services:
                        draw_matrix_services(screen, B_y)
                if cursor.colliderect(bt_more.rect):
                    d_y -= scroll_
                    n_y -= scroll_
                    Inv_y -= scroll_
                    C_y -= scroll_
                    E_y -= scroll_
                    L_y -= scroll_
                    B_y -= scroll_
                    add_row_matrix(screen, B_y)
                if cursor.colliderect(bt_less.rect):
                    d_y += scroll_
                    n_y += scroll_
                    Inv_y += scroll_
                    C_y += scroll_
                    E_y += scroll_
                    L_y += scroll_
                    B_y += scroll_
                    eliminate_row_matrix(screen,B_y)
                if cursor.colliderect(bt_equal.rect):
                    draw_matrix(screen, B_y)
                    sub_input.edit_text(str(sub_total))
                    a = tax_input.get_text()
                    if a != "":
                        print(a)
                        print(sub_total)
                        to = sub_total+((int(a)/100)*sub_total)
                        total_input.edit_text(str(to))
    pygame.quit()
    
make_invoice_window()
#show_services()