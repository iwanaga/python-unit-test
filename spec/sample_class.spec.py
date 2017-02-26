from expects import *

from lib.sample_class import *

with describe('SampleClass'):
    # before.each のブロック内は、同じ階層以下のテスト実行前に毎回実行されます
    with before.each:
        self.target = SampleClass(10)

    with describe('コンストラクタ'):
        with context('引数が文字列'):
            # 例外発生処理のテスト例
            with it('TypeError'):
                expect(lambda: SampleClass("string")).to(raise_error(TypeError))

    with describe('add'):
        # 状態を変える処理のテスト例
        with it('引数で指定した数を足して返す'):
            # before
            expect(self.target.number).to(equal(10))
            # 返り値
            expect(self.target.add(5)).to(equal(15))
            # after
            expect(self.target.number).to(equal(15))

    with describe('http_get'):
        # 通信やファイル入出力など、IO 処理が関わるときのテスト例
        with context('200 OK'):
            with it('Trueを返す'):
                expect(True).to(equal(True))

        with context('404 Not Found'):
            with it('Falseを返す'):
                expect(False).to(equal(False))
