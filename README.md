# SQLite-ETL-Destination
Specifically, the lab focuses on extracting keywords from transcriptions using the Keyword Extractor Tool and creating hashtags using the Hashtag Tool.




#### B. **Goals:**
By the end of this lab, learners should be able to:
1. Understand how to use command-line tools in Python.
2. Extract keywords f## Projects for Specialization

### ETL (Extract, Transform, Load)

# Keyword Extractor Tool to HashTag Tool (Lab 1)

#### A. **Overview:**
In this lab, learners will gain hands-on experience with command-line tools in Python to perform ETL tasks. Specifically, the lab focuses on extracting keywords from transcriptions using the Keyword Extractor Tool and creating hashtags using the Hashtag Tool.
rom a transcription using the Keyword Extractor Tool.
3. Create hashtags using the Hashtag Tool.
4. Limit the number of keywords to a maximum of the top keywords.

#### C. **Getting Started:**
1. Examine the `text.txt` file, a transcription of a video.
2. Run the command `python main.py --help` to view the available tools: `extract` and `hashtags`.
3. Use the `extract` tool to convert the text into keywords and observe the output.
4. Use the `hashtags` tool to create hashtags from the extracted keywords and observe the output.
5. Add a flag to the command-line tool to limit the number of keywords to a maximum of the top keywords.
6. Practice using the tools with text from various online sources like Wikipedia pages or blog posts.

#### D. **Advice:**
- Take time to read through the instructions carefully before starting each task.
- Use the provided command-line tools to assist with each task.
- Refer to the module's learning objectives to ensure progress is on track.
- Engage in practice with different types of text to fully understand the capabilities of the tools.

#### E. **Reflections on What You Learned When Done:**
1. Insight into the real-world applications of ETL processes and how they can be implemented using command-line tools in Python.
2. Understanding the techniques for extracting keywords and creating hashtags from textual data.
3. Practical experience with building and using command-line interfaces in Python.
4. Realizing the importance of tailoring information extraction to specific needs, like limiting the number of top keywords.
5. Recognition of how these ETL tools could be applied in various domains, such as social media analysis, SEO, and content summarization.

#### F. **Reference:**
- [GitHub Repository](https://github.com/nogibjj/coursera-applied-data-eng-projects)

**End of Lab One**

**Start Lab Two**

### SQLite Destination Lab

#### **Overview:**
In this lab, you will work with the `etl.py` command-line tool to extract keywords from a text file and load them into a SQLite database. You will then query the database and customize the tool to return a specific number of results.

#### **Tasks:**
1. **First**, run the `python etl.py` command and observe the three commands available: `delete`, `etl`, and `query`.
2. **Execute the ETL command** by running `python etl.py etl` to extract the keywords from the text file and load them into the SQLite database.
3. **Query the database** to return the top results with `python etl.py query`.
4. **Customize the tool** to return only five results by changing the command-line flag.
5. **For further practice**, create your own version of the tool in GitHub and extend the database with different metadata using another NLP tool.


#### **Reflections on What You Learned When Done:**
1. Experience in extracting data from text files and loading them into an SQLite database using a command-line tool.
2. Understanding how to query a database using a custom Python script.
3. Developing the ability to customize command-line tools to meet specific requirements.
4. Insight into extending existing tools and integrating other technologies like NLP.

#### **References:**
- [GitHub Repository](https://github.com/nogibjj/coursera-applied-data-eng-projects)

