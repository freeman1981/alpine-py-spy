# PY-SPY alpine based image

Thank you very much for [this](https://github.com/benfred/py-spy)! The repository describes how to use it.

I don't know how this thing works, but it works!
(It's a pity that it is not included with the python)

Build image for example `alpspy` (used in example)

`docker build -t alpspy`

Here is an example for a very special case.

`docker run -it --rm -v $(pwd):/src python:alpine python /src/script.py`

Get process pid from host point of view

`ps aux | grep script`

Run to get `/tmp/spy/profile.svg`

`sudo docker run -it --rm --pid="host" --privileged -v /tmp/spy:/tmp/spy alpspy py-spy record -o /tmp/spy/profile.svg --pid <PID>`

After waiting a while, press `ctrl+c`. 
Let's go look at the picture and see what we expected - the function `slow` was executed the longest.
Then you can analyze `/tmp/spy/profile.svg`, for example, understand which parts of the code "slow down".
