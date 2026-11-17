# LLM-wiki — база знаний Цифровой кафедры

Экземпляр 2 (МЖ-МИЭП, вариант Б). LLM Wiki по ФЛМК-образцам с акцентом на культурологию, сравнение Бахтин/Вяземский и шпаргалку билетов.

## Как открыть

1. Установите [Obsidian](https://obsidian.md).
2. Open folder as vault → выберите эту папку `LLM-wiki`.
3. Начните с `wiki/index.md`.

## Как сдавать в GitVerse Lab

В Kodik откройте терминал в этой папке (не делайте `git clone` задания Lab) и выполните:

```bash
git remote set-url origin <SSH-ссылка из GitVerse Lab>
git status
git add .
git commit -m "LLM-wiki"
git push origin main
```

Если `main` защищён:

```bash
git checkout -b wiki
git add .
git commit -m "LLM-wiki"
git push origin wiki
```

## Что уже сделано

- Импортированы 2 источника в `raw/учебные-материалы/`
- Собран слой `wiki/`: домены, концепции, персоналии, сравнения, обзор
- Заполнены `index.md` и `log.md`
