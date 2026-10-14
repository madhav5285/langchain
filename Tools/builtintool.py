from langchain_community.tools import DuckDuckGoSearchRun
#DuckDuckGoSearchRun-to search in real time
search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('top cricket headlines')

#print(results)


from langchain_community.tools import ShellTool
#to interact with cmd
shell_tool = ShellTool()

results = shell_tool.invoke('dir')

print(results)