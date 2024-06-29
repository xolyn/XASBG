# XASBG
![image](https://github.com/xolyn/XASBG/assets/118642042/3ef82799-80a4-4025-9fdf-46b558f35423)

An extremely light weight and simple static blog generator and content management system.

## Introduction 
**XASBG** stands for **X**ASBG is **A**nother **S**tatic **B**log **G**enerator. It allows you to be immersed in content creation and will automatically management all your post and show them in the the homepage. It's extremely lightweight and simple, you don't even need to set any configuration `.yaml` or `.xml` files! Just write your articles and build, static webpage files are ready in a second for uploading to any hoster like Cloudflare R2, Amazon S3, etc. 

## How to use
### Prereq.
1. `python 3.8+` for walrus operation
2. Python package `markdown` installed

That's it. Minimal dependencies!

### Build your site
Navigate to your project folder. 3 demos are added in `./post/` folder for your reference if you **have no experience with markdown** or you want to explore extra functionalities of XASBG! 

After you view them (or not), remove those demo markdown files. (~~You can keep them if you want~~) Write or move your article in markdown to the `./post/` folder. 

You may choose to add a metadata section in the beginning of a markdown file like this:

```
<!-- title: Article
time: 1997-09-11
category: life, travel -->
```

> You can simply type the following and comment them using `CTRL+/`
> ```
> title: ...
> time: ...
> category: ...
> ```
>
> ***Make sure you use comma to separate categories!***

So that the builder will automatically show these on the homepage and also on the title of html file.

**If you are not willing to do so, don't bother**, focus on content creation instead! The builder will automatically set the title as the name of the markdown file and the time as the last time you modify the markdown file! 

After you get all your markdown files in the `./post/` folder, execute `compile.py`. You can simply type `python compile.py` in the cmd started under this folder.

Some prompts will show up like this

```
   _  __ ___   _____ ____  ______
  | |/ //   | / ___// __ )/ ____/
  |   // /| | \__ \/ __  / / __
 /   |/ ___ |___/ / /_/ / /_/ /
/_/|_/_/  |_/____/_____/\____/
                      Build 1.0.1

Welcome to use XASBG.

Seems you haven't set your site name yet. Press 'S' to set it, or press 'M' to see more options:
```

You can now type `S` to set the site name (recommended for first build). You are allowed to change that later.

You can also type `M` to see the menu like this:
```
+---+----------------+
| B |  Build Site    |
+---+----------------+
| S |  Set Site Name |
+---+----------------+
| E |  Exit          |
+---+----------------+  
| M |  Menu          |
+---+----------------+
```

> More functionalities (e.g. favicon, etc.) will be added in the future.

If you believe everything is already, press `B` and check out the files `./site/` folder. (You don't need to create one, the builder will do it for you if you haven't)

Everything is done now. Host your webpages!
