# Technický popis

Kód je strukturován do několika tříd, které jsou v příslušných souborech. Výjimkou je soubor *main.py*, který pouze spouští hru. Nepopisuji jednotlivé funkce a proměnné, protože z kódu je patrné, co dělají. Jediná použitá externí knihovna je PyGame.

## Game

Třída reprezentuje hru jako takovou. Primárně zajišťuje běh hry.

## Scene

Scénou se v kontextu této aplikace rozumí souhrn věcí, který se má v danou chvíli vykreslit na obrazovce. Zároveň obsahuje logiku, která tyto věci ovládá. Objekty pro zobrazení jsou v proměnné `screen_objects`. Každý musí mít funkce `draw`, `on_click`, `on_hover`, `on_hover_leave`.

## Menu

Reprezentuje scénu, která je hlavní nabídkou aplikace.

## Pexeso

Reprezentuje scénu, kde se odehrává hra pexesa.

## Action rect

Action rect je rozšířením třídy Rect z PyGame, které reaguje na myš a umí samo sebe vykreslit.

## Text rect

Má vlastnosti jako Action rect a obsahuje text, který do svého středu vykreslí.

## Pexeso rect

Speciální rozšíření Text rect určené pro hru pexesa.
