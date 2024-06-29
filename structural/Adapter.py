class Target:
    def request(self) -> str:
        return "Target: The default target's behavior"


class Adaptee:
    @staticmethod
    def specific_request() -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):

    def request(self) -> str:
        return f"Adapter: (TRANSLATE) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    print(target.request())


if __name__ == "__main__":
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    adapter = Adapter()

    client_code(adapter)