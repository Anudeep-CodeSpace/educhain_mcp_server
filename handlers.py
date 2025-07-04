# handlers.py
# used to handle tool calls and resource requests
# Do not initialize the mcp server here! instead import it from server.py

# Handle resources along with info about the server
from schema.mcq import MCQRequest, MCQResponse
from schema.lessonplan import LessonPlanResponse
from schema.flashcard import FCRequest, FCResponse
from server import llm_client as client
from pydantic import Json


def handle_resources(mcp):
	# List available resources
	@mcp.resource('list://resources')
	def list_resources() -> dict:
		"""Returns a list of all the resources in the server."""
		return {
			'resources': [
				{
					"uri": "hello://world",
					"name": "Hello world resource",
					"description": "Sample hello world! resource for testing",
					"mime_type": "text/plain"
				},
				{
					"uri": "greetings://{name}",
					"name": "Send greetings",
					"description": "Send personalized greetings to a given name",
					"mime_type": "text/plain"
				},
				{
					"uri": "lessonplan://{subject}",
					"name": "Device lesson plan",
					"description": "Device a lesson plan for a given subject",
					"mime_type": "LessonPlanResponse",
					"examples": [
						"lessonplan://algebra",
						"lessonplan://math"
					] 
				}
			]
		}
	
	# Get detailed information about the MCP server
	@mcp.resource('about://info')
	def get_info() -> dict:
		"""Relay information about the MCP server."""
		return {
			"name": "Educhain - MCP server",
			"description": "A simple Educhain based MCP server that uses google gemini 1.5 flash to perform various tasks.",
			"version": "0.1.0",
			"tools": ["generate_mcq", "generate_flashcard"],
			"resources": ["list_resources", "get_info", "devise_lessonplan"],
			"creator": "Bandi Anudeep Reddy (github: Anudeep-CodeSpace)"
		}
	
	# Devise a lessonPlan for a given subject
	@mcp.resource('lessonplan://{topic}')
	def devise_lessonplan(topic: str) -> LessonPlanResponse:
		"""Devises a lesson plan to teach about any topic/subject"""
		result = client.content_engine.generate_lesson_plan(
			topic = topic,
			prompt_template = """
			Your task is to generate a lesson plan about a given topic.
			topic = {topic}
			"""
		)
		return LessonPlanResponse.model_validate(result.model_dump())

	

def handle_tools(mcp):
	# MCQ generation tool
	@mcp.tool()
	def generate_mcq(request: MCQRequest) -> MCQResponse:
		"""Tool to generate Multiple Choice Questions(mcqs) about a given topic."""
		result = client.qna_engine.generate_questions(
			topic = request.topic,
			num = request.num,
			prompt_template='''
			Your task is to generate {num} multiple choice questions about the given topic.
			topic = {topic}.
			'''
		)

		return MCQResponse.model_validate(result.model_dump())
	
	# Flash card generation tool
	@mcp.tool()
	def generate_flashcard(request: FCRequest) -> FCResponse:
		"""Tool to generate Flash cards about a given topic."""
		result = client.content_engine.generate_flashcards(
			topic = request.topic,
			num = request.num,
			prompt_template='''
			Your task is to generate {num} flash cards about the given topic.
			topic = {topic}
			'''
		)

		return FCResponse.model_validate(result.model_dump())
	
