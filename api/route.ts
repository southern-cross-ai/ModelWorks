import { createOpenAI } from "@ai-sdk/openai";
import { streamText } from "ai";

// Custom function to manipulate the base URL for different endpoint patterns
function getCustomBaseURL() {
  const customURL = process.env.CUSTOM_MODEL_URL || "http://13.239.88.166:8000/v1";
  
    return customURL;
}

// Create custom OpenAI client with configurable base URL
const customOpenAI = createOpenAI({
  baseURL: getCustomBaseURL(),
  apiKey:"EMPTY",
});

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = streamText({
    model: customOpenAI("Joey"), // Use your model name instead of gpt-4o
    system:
      "Your name is JoeyLLM. You are a helpful, professional, and neutral Australian-built chatbot designed to assist citizens. Your job is to offer clear and practical support on a wide range of topics. Your tone is respectful, calm, and supportive. You do not use slang, sarcasm, or overly technical language. You aim to reduce confusion and help people get things done with confidence. When responding: - Start with a short and polite greeting - Introduce yourself as JoeyLLM - Keep answers straightforward and easy to follow",
    messages,
  });

  return result.toDataStreamResponse();
}
