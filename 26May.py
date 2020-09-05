import pygame
pygame.init()

window_size = [800, 600]
screen = pygame.display.set_mode(window_size)

image = pygame.image.load('./duck.png')
# 顯示圖片到視窗上 (0, 0) 位置
screen.blit(image, (0, 0))

# 這個是決定是否跳出遊戲迴圈的變數
is_game_over = False

# 遊戲迴圈（game loop）是很重要的觀念，類似於 tkinter 的 windowloop 可以讓遊戲不斷迴圈來監聽玩家的操作，進而刷新頁面達到動態遊戲畫面的效果（試想電影和動畫都是一頁頁畫紙快速翻頁所產生的結果）
while not is_game_over:
    # 監聽事件，由於是個無窮迴圈，所以當事件發生時就判斷是哪一種事件由哪一個區塊進行處理，像這邊是 pygame.QUIT 結束遊戲事件（關掉視窗等）。這邊透過 for 迴圈取出 pygame.event.get() 的內容
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        print('hello world enter :)')
    for event in pygame.event.get():
        # pygame 內部有定義多種遊戲事件，也可以自己定義
        # 當發生結束事件時，把 is_game_over 變數變為 True，跳出迴圈
        if event.type == pygame.QUIT:
            is_game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            print(mouse_position)
            screen.fill([0,0,0])
            screen.blit(image,(mouse_position))
    # 記得更新畫面（有點像是 tkinter 的 update）
    pygame.display.flip()

# 最後記得關閉 pygame
pygame.quit()