global_code_one="""

#include <stdio.h>
#include <string.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <stdbool.h>

int pencereOlustur() {
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        printf("SDL_Init Error: %s \\n", SDL_GetError());
        return 1;
    }

    if (TTF_Init() == -1) {
        printf("TTF_Init Error: %s \\n", TTF_GetError());
        SDL_Quit();
        return 1;
    }

    SDL_Window *win = SDL_CreateWindow("Kedi UI", 200, 200, 800, 600, SDL_WINDOW_SHOWN);
    if (!win) {
        printf("Window Error: %s \\n", SDL_GetError());
        return 1;
    }

    SDL_Renderer *ren = SDL_CreateRenderer(win, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (!ren) {
        printf("Renderer Error: %s \\n", SDL_GetError());
        SDL_DestroyWindow(win);
        SDL_Quit();
        return 1;
    }

    TTF_Font *font = TTF_OpenFont("/usr/share/fonts/Adwaita/AdwaitaSans-Italic.ttf", 28);
    if (!font) {
        printf("Font Error: %s \\n", TTF_GetError());
        SDL_DestroyRenderer(ren);
        SDL_DestroyWindow(win);
        SDL_Quit();
        return 1;
    }

    SDL_Color white = {255, 255, 255};
    SDL_Surface *textSurface = TTF_RenderText_Blended(font, "Kedi UI Paneline Hoş Geldin!", white);
    SDL_Texture *textTexture = SDL_CreateTextureFromSurface(ren, textSurface);

    SDL_Rect textRect = { 100, 50, textSurface->w, textSurface->h };
    SDL_FreeSurface(textSurface);

    SDL_Rect button = { 300, 300, 200, 60 };

    bool running = true;
    SDL_Event event;

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) running = false;
        }

        // Arka plan rengi
        SDL_SetRenderDrawColor(ren, 20, 20, 30, 255);
        SDL_RenderClear(ren);

        // Yazıyı çiz
        SDL_RenderCopy(ren, textTexture, NULL, &textRect);

        // Butonu çiz
        SDL_SetRenderDrawColor(ren, 100, 100, 255, 255);
        SDL_RenderFillRect(ren, &button);

        // Buton üstüne yazı
        SDL_Surface *btnSurface = TTF_RenderText_Blended(font, "Başla", white);
        SDL_Texture *btnTexture = SDL_CreateTextureFromSurface(ren, btnSurface);
        SDL_Rect btnTextRect = { button.x + 50, button.y + 15, btnSurface->w, btnSurface->h };
        SDL_FreeSurface(btnSurface);
        SDL_RenderCopy(ren, btnTexture, NULL, &btnTextRect);
        SDL_DestroyTexture(btnTexture);

        SDL_RenderPresent(ren);
    }

    SDL_DestroyTexture(textTexture);
    TTF_CloseFont(font);
    SDL_DestroyRenderer(ren);
    SDL_DestroyWindow(win);
    TTF_Quit();
    SDL_Quit();

    return 0;
}







typedef struct 
{
    char *veri;
    int boyut;
    int kapasite;
} kedi_default_typedef_string;


kedi_default_typedef_string kedi_default_add_typedef_string(const char *first){
    int len = strlen(first);
    int kapasite = len + 1;
    kedi_default_typedef_string d;
    d.boyut = len;
    d.kapasite = kapasite;
    d.veri = malloc(kapasite);
    strcpy(d.veri, first);
    return d;
}

void kedi_default_assignment_typedef_string(kedi_default_typedef_string *d, const char *new_data){
    int len=strlen(new_data);
    if(len+1>d->kapasite){
        d->kapasite=len+1;
        d->veri = realloc(d->veri,d->kapasite);
    }
    strcpy(d->veri,new_data);
    d->boyut=len;
}


int yazı_karşılaştır(const char *str1, const char *str2) {
    while (*str1 && *str2) {
        if (*str1 != *str2) {
            return 0;  
        }
        str1++;
        str2++;
    } 
    return (*str1 == '\\0' && *str2 == '\\0');
}

"""