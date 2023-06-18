"""
`libc` command test module
"""

from tests.utils import (GefUnitTestGeneric, _target, find_symbol, gdb_run_cmd,
                         removeuntil)


class LibcCommand(GefUnitTestGeneric):
    """`libc` command test module"""


    def setUp(self) -> None:
        target = _target("default")
        return super().setUp()


    def test_cmd_libc(self):
        res = gdb_run_cmd("libc")

        self.assertNoException(res)
        self.assertIn("No debugging session active", res)

        res = gdb_run_cmd("libc", before=["b *main", "run"])
        res = res.split('\n')[-2:]

        self.assertIn("Libc Base: ", res[0])
        self.assertTrue(res[0].endswith("000"))
        self.assertIn("Libc Version: ", res[1])