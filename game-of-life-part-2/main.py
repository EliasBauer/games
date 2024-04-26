

                                           
def findAllNeighbors(cells, row_index ,cells_index):
   #neighbor left
      living_neighbors = 0
      if cells_index -1 >= 0 :
         n_left = cells[row_index][cells_index -1]
         if n_left=='x':
          living_neighbors += 1  
   #prüft, ob links ein nachbar ist
        
   #neighbor right 
      if cells_index + 1 < len(cells[row_index]):
         n_right = cells[row_index][cells_index +1]
         if n_right =='x':
            living_neighbors += 1
   #prüft, ob rechts ein nachbar ist
  
   #neighbor up 
      if row_index -1 >= 0 :
         n_up = cells[row_index-1 ][cells_index]
         if n_up=='x':
            living_neighbors += 1
   #prüft, ob oberhalb ein nachbar ist
   
   #neighbor down 
      if row_index + 1 < len(cells[cells_index]): 
         n_down = cells[row_index +1 ][cells_index]
         if n_down == 'x':
           living_neighbors += 1
   #prüft, ob links ein nachbar ist
  
   #diagonal lower right
      if row_index +1 < len(cells[cells_index]) and cells_index +1 < len(cells[row_index]):
         n_lower_right = cells[row_index +1][cells_index +1]
         if n_lower_right == 'x':
            living_neighbors += 1
   #prüft, ob unten rechts ein nachbar ist
  
   #diagonal lower left!
      if row_index +1 < len(cells[cells_index]) and cells_index -1 >= 0:
         n_lower_left = cells[row_index +1][cells_index -1]
         if n_lower_left == 'x':
            living_neighbors += 1
   #prüft, ob unten links ein nachbar ist
   
   
   #diagonal up left   
      if row_index -1 >= 0 and cells_index -1 >= 0:
         n_upper_left = cells[row_index -1][cells_index -1]
         if n_upper_left == 'x':
            living_neighbors += 1
   #prüft, ob oben links ein nachbar ist
  
   #diagonal up right   
      if row_index  -1 >= 0 and cells_index + 1 < len(cells[row_index]):
         n_upper_right = cells[row_index -1][cells_index +1] 
         if n_upper_right == 'x':
            living_neighbors += 1
      return living_neighbors
   #prüft, ob oben rechts ein nachbar ist
   
def createEmptyCells(original_cells):
   result = []
   for row in original_cells:
      row_list = []
      for i in range(len(row)):
         row_list.append('')
      result.append(row_list)#fügt zur original eingetippten liste der elemente hinzu
   return result
      

def gameOfLife(original_cells):#leere zellen für die neu-Konfiguration der zellen
   empty_cells = createEmptyCells(original_cells)#obere funktion wird aufgerufen
   new_cells = lifeAndDeath(empty_cells, original_cells) 
   for row in new_cells:
       print(row)
   return new_cells   #neue zellen für neue liste erstellt    
         
def lifeAndDeath(new_cells, original_cells):         
   for row_index, row in enumerate(original_cells):#zählt die Positionen hoch
      for cells_index, cell in enumerate(row):#zählt die reihen hoch
         if cell != 'x': #wenn die zelle tot ist
            neighbor = findAllNeighbors(original_cells, row_index ,cells_index)
            if neighbor == 3: #bei genau 3 nachbarn wird eine zelle 'geboren' ansonsten bleibt sie tot
               new_cells[row_index][cells_index] = 'x'
            else:
               new_cells[row_index][cells_index] = ' '   
         else: # wenn die zelle lebt
            neighbor = findAllNeighbors(original_cells, row_index ,cells_index)
            if neighbor < 2: #wenn eine zelle weniger als zwei nachbarn hat stirbt sie
               new_cells[row_index][cells_index] = ' '
            if neighbor == 2 or neighbor == 3 : #wenn eine zelle genau 2 oder 3 Nachbarn hat lebt sie weiter
               new_cells[row_index][cells_index] = 'x'   
            if neighbor > 3: #wenn eine zelle mehr als 3 nachbarn hat stirbt sie
               new_cells[row_index][cells_index] = ' '
   return new_cells
      
def formatCells(cell_string):#unterscheidet die eingegebenen Charaktere um eine Liste zu erstellen
   result = [[]]
   row = 0
   for char in cell_string:
      if char == ' ':
         result[row].append(' ')
      if char == 'x':
         result[row].append('x') 
      if char == ',':
         row = row + 1
         result.append([]) #neue liste (unten) hinzugefügt
   return result
           
     
#wenn (leer) dann in liste ' '
#wenn , dann row+1
#wenn x dann x in cell eintragen
def main():
   print("game of life")
   
   # für anzahl generationen
   number_generations = int(input('Number of Generations:'))
   #eingabe der Liste x/'
   cell_string = input('elements per row (space or x):')
   original_cells = formatCells(cell_string)
 
   print('start')
   for row in original_cells:
      print(row)
      
   for number_generations in range(number_generations):
      print('Generation: ', number_generations + 1)
      #zählt die Nummern der generationen hoch
      original_cells = gameOfLife(original_cells)
   print ('finish')   
   
main()
#wird aufgerufen