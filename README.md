# PY-SPY alpine based image

Thank you very much for [this](https://github.com/benfred/py-spy)! The repository describes how to use it.

I don't know how this thing works, but it works!
(It's a pity that it is not included with the python)

Here is an example for a very special case.
```bash
docker run -it --rm -v $(pwd):/src python:alpine python /src/script.py
```

Get process pid from host point of view
```bash 
ps aux | grep script.py
sudo docker run -it --rm --pid="host" --privileged -v /tmp/spy:/tmp/spy freeman1981/py-spy-alpine py-spy record -o /tmp/spy/profile.svg --pid <PID>
```

After waiting a while, press `ctrl+c`. 
Let's go look at the picture `/tmp/spy/profile.svg` and see what we expected - the function `slow` was executed the longest.
