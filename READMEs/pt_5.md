# PT. 5 - Adding CrewAI Agents

Now we’re going to add in some AI…

##

- Let’s update the `requirements.txt` to contain additional 3rd-party packages
- And update the `main.py` file to include this CrewAI-related code…
  
```sh
touch helpers/replace_yaml_variables.py
mkdir application_schema
touch application_schema/news_results.py
mkdir config
touch config/tasks.yaml
touch config/agents.yaml
```

- populate the replace_yaml_variables.py file
- populate the news_results.py
- populate the tasks.yaml
- populate the agents.yaml

And, of course, run `pip install -r requirements.txt`

##

If we look closely at this config folder, we can see we’re creating a group of agents specialized in reporting news about Haiti

We can easily tweak this config to report information about whatever niche matters to us btw, but this is what we’ll use for demonstration purposes

At the end of this walkthrough we’ll adjust these prompts to focus on reporting the latest news in the world of Insurance Technology

##

Anyways!

Let’s now run our application again and see what happens - `python main.py`

We can see an ERROR has been thrown due to a missing OPENAI_API_KEY

CrewAI, the Multi-Agent framework we’re using, supports a number of LLMs but by default uses OpenAI

If your new to all this Agent stuff, here’s a quick little diagram that sheds some light on what I just said…

An Agent, in the context of this video, is like a virtual person and an LLM acts as this virtual person’s brain

## 

We can get an OPENAI_API_KEY by coming over to https://platform.openai.com/ and signing up…

And after signing up, make sure to add some credits. OpenAI’s API is pay-per-use, just like a gas station, so you will need some credits.

I recommend adding whatever the minimum allowed amount is as the cost of what we’ll be doing will only be in the pennies

After adding credits, come over to the Dashboard > API keys section and create an API key

And let’s copy this API key’s value into our project by adding a new line in the .env file that reads, in all caps, 

```env
OPENAI_API_KEY=<API_KEY_HERE>
```

And when that’s all set up let’s run our script again and see what happens

`python main.py`

Alright! Things look like they’re working! This is great!

##

If we take a closer at the CrewAI code we just added, we can see we’re creating 2 Agents (A Manager Agent and a Researcher Agent) and 1 Task (performing research across a list of web pages)

This configuration gets tied together with the Crew object on line 56

##

As of the time of recording CrewAI let’s you run your Agents in 2 modes: Sequential Mode and Hierarchical Mode

Sequential Mode means the Agents will perform the tasks sequentially one-by-one. In Sequential Mode, you list your tasks in the tasks.yaml file and manually map each task to one of the agents in your project…

Hierarchical Mode, which is what we’re using at the moment, we delegate one of the Agents in our Crew as the “Manager” of the other Agents and then assign tasks to the Manager. The Manager Agent will break any tasks it receives into sub-tasks as needed and will automatically assign each sub-task to one or more of the Agents in the Crew.

Depending on the LLM and other implementation details, the reliability of Hierarchical Mode can be either impressive or atrocious BUT for the job of synthesizing information across a number of web pages in a particular niche, I found it to be a worthy match…

##

Let’s run our Crew a few times to get feel for what it’s doing…
Each time we run our Crew, we’ll add another website to this list of web pages and review the output

Using this report.md file is useful for debugging BUT we don’t need to track it as it will be generated on the fly. So let’s add it to the .gitignore

And yea things are looking good. So let’s move on to part 6 where we’ll send this A.I.-generated report via email to a list of “subscribers”…
