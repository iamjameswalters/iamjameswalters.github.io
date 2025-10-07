Title: A Little AI Experiment (Reading Handwriting and Counting Numbers)
Date: 2025-10-07
Category: AI
Tags: Kagi, AI, LLM

I did an interesting experiment last night, and I thought I'd share the results here for everyone. I was going through a set of 1,000 flash cards and making a note of which ones were missing. That resulted in this list:

<img src="{static}/images/missing_flash_cards.jpg" alt="A small notepad containing a list of numbers" style="max-width: 50%">

### The Prompt 💬️

I decided to throw this picture at a bunch of models in [Kagi Assistant](http://kagi.com/), along with this prompt:

> These numbers were missing from my set. How many does that make in total

### The Results 📃️

Here are all the models I tried, along with their answers, and how much the response cost:

- [ChatGPT 4.1](https://kagi.com/assistant/37a38cf0-267f-4e44-9c60-b56ba7a63b56) (71), $0.01
- [ChatGPT 5](https://kagi.com/assistant/7fda764f-fbf5-4fea-8a1a-d7c0137eee59) (77, correct), $0.04
- [Claude 4.5 Sonnet](https://kagi.com/assistant/ebd6f386-6e4e-4532-ab2c-05c35077e1d0) (121), $0.02
- [Claude 4.5 Sonnet (reasoning)](https://kagi.com/assistant/a38af95c-33a0-46ab-8054-76e511ab51d9) (74), $0.04
- [DeepSeek Chat V3.1 Terminus](https://kagi.com/assistant/6e808e5b-3b74-434d-b876-4174036911e2) (77, correct), $0.01
- [Gemini 2.5 Flash](https://kagi.com/assistant/61d58be1-b77a-493b-9d5b-365412b39b55) (70), $0.003
- [Gemini 2.5 Pro](https://kagi.com/assistant/59147e5c-c25a-409f-89da-081c7d830031) (67), $0.004
- [Grok 4](https://kagi.com/assistant/f1aac9bd-9b46-408b-be27-aebbba116da9) (77, correct), $0.03
- [Ki](https://kagi.com/assistant/9f79b8cc-0374-44cb-81a3-394fc525194b) (61), $0.009
- [Ki Fast](https://kagi.com/assistant/ffd69216-8bba-4e89-990c-c9654f74cd43) (64), $0.006
- [Kimi K2](https://kagi.com/assistant/727858e4-819d-421c-a33c-836103c5b9cf) (77, correct), $0.004
- [Llama 4 Maverick](https://kagi.com/assistant/802ba729-73e4-4ffc-9216-41c2680a6208) (74), $0.005
- [Mistral Medium](https://kagi.com/assistant/71cba7e8-6362-4bab-8419-ddfcbaebe540) (100), $0.003
- [Qwen 3 235B (reasoning)](https://kagi.com/assistant/43573661-5d29-4733-9970-07b2ba75260a) (77, correct), $0.004
- [Z GLM 4.5](https://kagi.com/assistant/0abffa49-2f5e-44f4-9cce-a07021e31f27) (79), $0.004

Those who got it correct, in order of cheapest:

1. Kimi K2, $0.004
2. Qwen 3 235B (reasoning), $0.004
3. DeepSeek Chat V3.1 Terminus, $0.01
4. Grok 4, $0.03
5. ChatGPT 5, $0.04

Common points of failure were not understanding what to do with the ranges (e.g. 9-14). Sometimes the models couldn't read my handwriting correctly, but this didn't actually matter (since I just wanted them to count how many I'd written down), _unless_ they thought they saw the same number written twice, and tried to correct by only counting it once.

Interesting to see the Chinese models doing well here, on the cheap. Grok 4 and GPT 5 will get you there, but for 3-10x cost.

<footer style="font-weight: bold; text-align: center;">
Found this interesting? <a href="https://ko-fi.com/iamjameswalters">Buy me a coffee!</a> ☕️
</footer>
