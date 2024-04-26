

                                           
def findeAlleNachbarn(zellen, reihen_index ,zellen_index):
   #nachbarn links
      lebende_nachbarn = 0
      if zellen_index -1 >= 0 :
         n_links = zellen[reihen_index][zellen_index -1]
         if n_links=='x':
         #  print("links gefunden")
          lebende_nachbarn += 1 
   #print('links','lebende_nachbarn', lebende_nachbarn) 
        
   #nachbarn rechts 
      if zellen_index + 1 < len(zellen[reihen_index]):
         n_rechts = zellen[reihen_index][zellen_index +1]
         if n_rechts =='x':
            lebende_nachbarn += 1
  
   #nachbarn oben 
      if reihen_index -1 >= 0 :
         n_oben = zellen[reihen_index-1 ][zellen_index]
         if n_oben=='x':
         # print("oben gefunden")
            lebende_nachbarn += 1
  
   
   #nachbarn unten 
      if reihen_index + 1 < len(zellen[zellen_index]): 
         n_unten = zellen[reihen_index +1 ][zellen_index]
         if n_unten == 'x':
           lebende_nachbarn += 1
  
   #diagonal unten rechts
      if reihen_index +1 < len(zellen[zellen_index]) and zellen_index +1 < len(zellen[reihen_index]):
         n_unten_rechts = zellen[reihen_index +1][zellen_index +1]
         if n_unten_rechts == 'x':
            lebende_nachbarn += 1
  
   #diagonal unten links!
      if reihen_index +1 < len(zellen[zellen_index]) and zellen_index -1 >= 0:
         n_unten_links = zellen[reihen_index +1][zellen_index -1]
         if n_unten_links == 'x':
            lebende_nachbarn += 1
   
   
   #diagonal oben links   
      if reihen_index -1 >= 0 and zellen_index -1 >= 0:
         n_oben_links = zellen[reihen_index -1][zellen_index -1]
         if n_oben_links == 'x':
            lebende_nachbarn += 1
  
   #diagonal oben rechts   
      if reihen_index  -1 >= 0 and zellen_index + 1 < len(zellen[reihen_index]):
         n_oben_rechts = zellen[reihen_index -1][zellen_index +1] 
         if n_oben_rechts == 'x':
            lebende_nachbarn += 1
      return lebende_nachbarn
   
def createEmptyCells(original_cells):
   result = []
   for row in original_cells:
      row_list = []
      for i in range(len(row)):
         row_list.append('')
      result.append(row_list)
   return result
      

def gameOfLife(original_cells):
   leere_zellen = createEmptyCells(original_cells)
   neue_zellen = lifeAndDeath(leere_zellen, original_cells) 
   for reihe in neue_zellen:
       print(reihe)
   return neue_zellen       
         
def lifeAndDeath(neue_zellen, original_cells):         
   for reihen_index, reihe in enumerate(original_cells):
      for zellen_index, zelle in enumerate(reihe):
      # print('\n\nreihe:',reihen_index, 'index:',zellen_index)
         if zelle != 'x': # wenn wir tot sind
            nachbarn = findeAlleNachbarn(original_cells, reihen_index ,zellen_index)
            if nachbarn == 3:
               neue_zellen[reihen_index][zellen_index] = 'x'
            else:
               neue_zellen[reihen_index][zellen_index] = ' '   
         else: # wenn wir leben
            nachbarn = findeAlleNachbarn(original_cells, reihen_index ,zellen_index)
            if nachbarn < 2:
               neue_zellen[reihen_index][zellen_index] = ' '
            if nachbarn == 2 or nachbarn == 3 :
               neue_zellen[reihen_index][zellen_index] = 'x'   
            if nachbarn > 3:
               neue_zellen[reihen_index][zellen_index] = ' '
   return neue_zellen
      
def formatCells(cell_string):
   result = [[]]
   row = 0
   for char in cell_string:
      if char == ' ':
         result[row].append(' ')
      if char == 'x':
         result[row].append('x') 
      if char == ',':
         row = row + 1
         result.append([])
   return result
           
     
#wenn (leer) dann in liste ' '
#wenn , dann reihe+1
#wenn x dann x in zelle eintragen
def main():
   print("game of life")
   
   # für anzahl generationen
   number_generations = int(input('Anzahl der Generationen:'))
   cell_string = input('5 elemente pro reihe (leerzeichen('') oder x):')
   original_cells = formatCells(cell_string)
 
   print('start')
   for reihe in original_cells:
      print(reihe)
      
   for number_generations in range(number_generations):
      print('Generation: ', number_generations + 1)
      original_cells = gameOfLife(original_cells)
   print ('finish')   
   
main()
