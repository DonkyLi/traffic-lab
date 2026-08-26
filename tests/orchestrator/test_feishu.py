import unittest

from orchestrator.feishu import parse_event


class FeishuEventTests(unittest.TestCase):
    def test_challenge_event_is_returned_without_creating_task(self):
        result = parse_event({"challenge": "abc", "token": "token"}, "token")
        self.assertEqual(result.kind, "challenge")
        self.assertEqual(result.text, "abc")

    def test_message_event_extracts_text_from_json_content(self):
        payload = {
            "header": {"event_id": "evt-1"},
            "event": {"message": {"content": '{"text":"/需求 做 L1"}'}} ,
        }
        result = parse_event(payload, "")
        self.assertEqual(result.kind, "message")
        self.assertEqual(result.text, "/需求 做 L1")
        self.assertEqual(result.event_id, "evt-1")


if __name__ == "__main__":
    unittest.main()
