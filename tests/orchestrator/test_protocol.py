import unittest
import hashlib
import hmac

from orchestrator.protocol import parse_feishu_text, verify_feishu_signature


class ProtocolTests(unittest.TestCase):
    def test_parse_new_task_command(self):
        command = parse_feishu_text("/需求 做一个 L1 道路连接关卡")
        self.assertEqual(command.kind, "task")
        self.assertEqual(command.text, "做一个 L1 道路连接关卡")

    def test_parse_status_command(self):
        command = parse_feishu_text("/状态")
        self.assertEqual(command.kind, "status")

    def test_signature_is_verified_with_hmac(self):
        body = b'{"challenge":"abc"}'
        signature = hmac.new(b"secret", body, hashlib.sha256).hexdigest()
        self.assertTrue(signature)
        self.assertTrue(verify_feishu_signature(body, "secret", signature))
        self.assertFalse(verify_feishu_signature(body, "secret", "wrong"))


if __name__ == "__main__":
    unittest.main()
