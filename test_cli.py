def test_cli(page):
    page.goto("https://youtube.com")

    # CLI COMMANDS
    # playwright codegen https://youtube.com --save-storage=auth.json
    # save all the cookies to auth.json file
    # playwright open --load-storage=auth.json -whatever app
    # playwright pdf https://en.wikipedia.org/wiki/PDF wiki.pdf
