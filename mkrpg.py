"""
Matt Knouff, CSCI N451, Final Project

A small RPG game
"""

import pygame, random, character
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640,480))

# ATTACK METHOD
def attack(user, opponent, background,value):
    fightText = FightLabel()
    fight = pygame.sprite.Group(fightText)
    keepGoing = True
    value = value
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if user.hitPoints > 0:
                        if opponent.hitPoints > 0:
                            fightS = pygame.mixer.Sound("fight.wav")
                            fightS.play()
                            damageOther = (random.randrange(0,2) * user.attackSkill)
                            opponent.hitPoints -= damageOther
                            damageSelf = (random.randrange(0,2) * opponent.attackSkill)
                            user.hitPoints -= damageSelf
                            fightText.text = "Opponent -%d HP. Opponent's Total HP: %d. You -%d HP. Your Total HP: %d." % (damageOther,opponent.hitPoints, damageSelf, user.hitPoints)
                            fight.clear(screen,background)
                            fight.update()
                            fight.draw(screen)
                            pygame.display.flip()
                        elif opponent.hitPoints <= 0:
                            fightText.text = "You have won!"
                            fight.clear(screen,background)
                            fight.update()
                            fight.draw(screen)
                            pygame.display.flip()
                            if value == 0:
                                opponent.death()
                                user.xp += opponent.xp
                                keepGoing = False
                            else:
                                fightText.text = "You have defeated level 1!"
                                fight.clear(screen,background)
                                fight.update()
                                fight.draw(screen)
                                pygame.display.flip()
                    elif user.hitPoints <= 0:
                        fightText.text = "You have died!"
                        fight.clear(screen,background)
                        fight.update()
                        fight.draw(screen)
                        pygame.display.flip()
                        user.lives -= 1
                        if user.lives <= 0:
                            fightText.text = "Game Over"
                            fight.clear(screen,background)
                            fight.update()
                            fight.draw(screen)
                            pygame.display.flip()
                            user.death()
                            keepGoing = False
                        elif user.lives > 0:
                            user.reset()
                            keepGoing = False

# INSTRUCTIONS / TITLE SCREEN
def instructions():
    insFont = pygame.font.SysFont("Times New Roman", 24)
    instructions = (
        " ",
        "MK RPG",
        " ",
        "Arrow keys control movement.",
        "'A': Attack",
        "'SPACEBAR': Talk",
        "'M': Action key (only works on some items/characters)",
        " ",
        "Press 'c' to continue..."
    )
    insLabels = []
    for line in instructions:
        tempLabel = insFont.render(line, 1, (0,255,0))
        insLabels.append(tempLabel)
    keepGoing = True
    clock = pygame.time.Clock()
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    keepGoing = False
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))
        pygame.display.flip()
    keepGoing = True
    return keepGoing

# LABEL FOR USER STATS
class Label(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Terminal", 16)
        self.text = ""
        self.center = (65,40)           
    def update(self):
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

# LABEL FOR MESSAGES FROM SYSTEM DURING GAME, OTHER CHARACTERS, AND USER
class FightLabel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Times New Roman", 20)
        self.text = ""
        self.center = (320,440)        
    def update(self):
        self.image = self.font.render(self.text, 1, (255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

# MAIN LOOP
def main():
    # SET CAPTION
    pygame.display.set_caption("MK RPG")
    # CALL INSTRUCTIONS + SET BACKGROUND IMAGE
    instructions()
    background = pygame.image.load("images/environments/lvl01-carpet.jpg")
    background = background.convert()
    screen.blit(background,(0,0))
    # SPRITES, ETC
    user = character.User(screen)
    girl = character.MentallyIllWoman(screen)
    farmer = character.DrunkHusband(screen)
    corpse = character.CorpseLady(screen)
    mush = character.Mushroom(screen)
    stats = Label()
    messages = FightLabel()
    message = pygame.sprite.Group(messages)
    allSprites = pygame.sprite.Group(girl,farmer,corpse,user,stats)
    # GAME LOOP
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if user.rect.colliderect(girl.rect):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        messages.text = "MENTALLY ILL WOMAN: I don't want meds! You're fired.  You and your stupid hair are fired."
                        message.clear(screen, background)
                        message.update()
                        message.draw(screen)
                        pygame.display.flip()
                    elif event.key == pygame.K_a:
                        message.clear(screen,background)
                        attack(user,girl,background,0)
                    elif event.key == pygame.K_m:
                        girl.hitPoints = 0
                        girl.death()
                        user.xp += (girl.xp / 2)
                        messages.text = "Risperdal has made Mentally Ill Woman fall asleep."
                        message.clear(screen, background)
                        message.update()
                        message.draw(screen)
                        pygame.display.flip()
            if user.rect.colliderect(farmer.rect):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        messages.text = "HUSBAND: Give me money!"
                        message.clear(screen, background)
                        message.update()
                        message.draw(screen)
                        pygame.display.flip()
                    elif event.key == pygame.K_a:
                        message.clear(screen,background)
                        attack(user,farmer,background,0)
                    elif event.key == pygame.K_m:
                        messages.text = "HUSBAND: You don't have money, you scoundral!"
                        message.clear(screen, background)
                        message.update()
                        message.draw(screen)
                        pygame.display.flip()
                        farmer.hitPoints *= 2
                        farmer.attackSkill *= 2
                        attack(user,farmer,background,0)
            if user.rect.colliderect(corpse.rect):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        messages.text = "Hello Victor! Don't make fun of blind people!"
                        message.clear(screen, background)
                        message.update()
                        message.draw(screen)
                        pygame.display.flip()
                    elif event.key == pygame.K_a:
                        message.clear(screen,background)
                        attack(user,corpse,background,0)
            if farmer.hitPoints <= 0:
                if girl.hitPoints <= 0:
                    if corpse.hitPoints <= 0:
                        background = pygame.image.load("images/environments/lvl01-carpetE.jpg")
                        background = background.convert()
                        screen.blit(background,(0,0))
                        allSprites = pygame.sprite.Group(mush,user,stats)
                        if user.rect.colliderect(mush.rect):
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    messages.text = "MUSHROOM: Eat me!"
                                    message.clear(screen, background)
                                    message.update()
                                    message.draw(screen)
                                    pygame.display.flip()
                                elif event.key == pygame.K_a:
                                    message.clear(screen,background)
                                    attack(user,mush,background,1)
                                elif event.key == pygame.K_m:
                                    messages.text = "I'm poisionous!"
                                    message.clear(screen, background)
                                    message.update()
                                    message.draw(screen)
                                    user.lives -= 1
                                    pygame.display.flip()
            stats.text = "XP:%d|Lives:%d|HP:%d/%d" % (user.xp, user.lives, user.hitPoints, user.hitPointsMax)
        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()
