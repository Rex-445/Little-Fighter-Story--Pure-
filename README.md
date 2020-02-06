# Little-Fighter-Story--Pure-

After installing the project, there will be some funny errors in bliting the sprites of characters                                         

Don't worry too much it's an easy fix:                                                                                              

* open the "char_anims". Hit "Alt + M" to open the Python Module search.                                                                    
* search "pygame.sprite". then in the script search for a class called "LayeredUpdates()"                                                                                        
* under "LayeredUpdates()" search for "draw()"                                                                                            
* there should be a line that says "newrect = surface_blit(spr.sprite, spr.rect)" change it to "newrect = surface_blit(spr.bdy, spr.rect)"
* that should definitely fix the problem. And perharps u understand what caused it to act that way XD


THANKS FOR DOWNLOADING!
You are Breathtaking

#Requirements 
Python 
Pygame
