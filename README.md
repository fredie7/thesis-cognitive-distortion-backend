## THESIS: CONVERSATIONAL AI FOR COGNITIVE DISTORTIONS

### ABSTRACT
Cognitive distortions are dreadful, recurring negative thought patterns. They
are a silent yet powerful force behind declining mental health that could
pave the way for prolonged emotional distress, often culminating in depression
if left unchecked. This thesis attacks this growing concern by introducing
a Conversational AI-powered application that detects these distortions while
engaging in chat exchanges with students.
The research begins with identifying the ten most common cognitive distortions,
such as all-or-nothing thinking, overgeneralization, emotional reasoning,
labelling, personalization, mind-reading, fortune-telling, magnification also
known as catastrophizing, should statements, and mental filter. The functionality
ties an LLM to a retrieval-augmented generation mechanism that incorporates
a vector database, ensuring contextually grounded responses through recursive
document splitting and history-aware retrievers. Ultimately, it integrates prompt
engineering techniques to rationalize messages fraught with cognitive nuances
from users.
The resulting system takes the form of an intelligent chatbot assistant that
provides a supportive space where University of Oulu students can reflect on their
thoughts in order to foster cognitive self-awareness and reduce mental distress
through soothing chat engagement

### METHODOLOGY
The study began with a pre-questionnaire aimed at assessing students’ perspectives on engaging with a conversational agent designed to identify cognitive distortions. Results showed that 55.5% of participants were enthusiastic about sharing self-critical thoughts with the chatbot, and 61.1% expressed willingness to use the chatbot for short-term stress relief. 

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/fredie7/thesis-cognitive-distortion-backend/blob/main/pre-study%20likert%20analysis.png?raw=true" alt="Likert Analysis" width="300" />
      <br />
      <strong>Likert Scale Analysis</strong>
    </td>
    <td align="center">
      <img src="https://github.com/fredie7/thesis-cognitive-distortion-backend/blob/main/pre-study%20analysis.png?raw=true" alt="Pre-study Analysis" width="300" />
      <br />
      <strong>Pre-study Analysis Summary</strong>
    </td>
  </tr>
</table>


As development progressed to the halfway point, a think-aloud test was conducted to gather valuable insights from students, focusing on the chatbot’s usability and areas for improvement. After the chatbot was fully developed, a post-study questionnaire was administered to evaluate user experience using the User Experience Questionnaire (UEQ). Emotional engagement was further analyzed through cluster analysis, word clouds, and content analysis.

### SYSTEM ARCHITECTURE
<p align="center">
  <img src="https://github.com/fredie7/thesis-cognitive-distortion-backend/blob/main/system%20architecture.png?raw=true" alt="System Architecture" width="600" />
  <br />
  <strong>System Architecture</strong>
</p>

The MED-45 model harnesses the power of retrieval augmented generation (RAG) and the GPT-4o model in a design architecture that strikes a balance between the speed and precision of the chat interactions. It incorporates a pipeline that reconciles conversational data and user input into vector representations before storing them in the database. The framework also integrates prompt engineering techniques to aid the return of appropriate responses, as well as memory management to ensure continuity across chat sessions between the AI and users. The model is deployed within a FastAPI framework to enable client-side interactivity.

### USER INTERFACE

<table align="center">
  <tr>
    <td align="center" style="padding: 10px;">
      <img src="https://github.com/fredie7/thesis-cognitive-distortion-backend/blob/main/landing%20page.png?raw=true" alt="Landing Page" width="250" />
      <br />
      <strong>Landing Page</strong>
    </td>
    <td align="center" style="padding: 10px;">
      <img src="https://github.com/fredie7/thesis-cognitive-distortion-backend/blob/main/dashboard.png?raw=true" alt="Dashboard" width="250" />
      <br />
      <strong>Dashboard View</strong>
    </td>
    <td align="center" style="padding: 10px;">
      <img src="https://github.com/fredie7/thesis-cognitive-distortion-backend/blob/main/chat%20interface.png?raw=true" alt="Chat Interface" width="250" />
      <br />
      <strong>Chat Interface</strong>
    </td>
  </tr>
</table>

### Link to thesis publication:
https://oulurepo.oulu.fi/handle/10024/57086

### Link to front-end repository:
https://github.com/fredie7/thesis-cognitive-distortion-frontend

