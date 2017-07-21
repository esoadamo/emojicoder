# Python Emojicoder

**Because who wants Python code in plain text?**

😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏

## What is this?

This is what allows you to convert all your boring plain text Python code into emojis!

Just run `python3 emojicoder.py --backup my_boring_code.py`

and have a new cool, modern and awesome file. Still fully runable. Try it!

`python3 my_boring_code.py`

Cool, isn't it?

P. S. if you are a mad man try running `emojicoder.py` with `--no-decoder` option 😉

## How?

When you run emojicoder it will not just encode whole file, but it will also add a minimalistic function that decrypts code back to boring Python (don't worry, it is done during runtime and just in memory)

## API?

Say no more!

```python
import emojicoder

boring_string = "hello emojis"
cool_string = emojicoder.encode(boring_string)  # encodes string to emojis
print(cool_string)
original_string = emojicoder.decode(cool_string)  # decodes emojis to plaintext string
print(original_string)
```
## I get it, but WHY?

Too much [/r/ProgrammerHumor](https://www.reddit.com/r/ProgrammerHumor), i guess