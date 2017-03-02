from expects import *
from unittest.mock import MagicMock
from unittest.mock import patch

import requests
from requests import Response

from lib.sample_class import *

with describe('SampleClass'):
    # before.each のブロック内は、同じ階層以下のテスト実行前に毎回実行されます
    with before.each:
        self.target = SampleClass(10)

    with describe('コンストラクタ'):
        with context('引数がinteger'):
            with it('インスタンスを生成'):
                expect(SampleClass(-1)).to(be_a(SampleClass))

        with context('引数がinteger以外'):
            with it('TypeError'):
                # 例外発生をテストする例。ラムダ式の中で実行することに注意。
                expect(lambda: SampleClass("dummy string")).to(raise_error(TypeError))

    with describe('is_even'):
        # 引数と返り値の正しさはテストしよう。仕様書の代わりになります。
        with context('self.numberが偶数'):
            with it('Trueを返す'):
                expect(SampleClass(2).is_even()).to(equal(True))

        with context('self.numberが奇数'):
            with it('Falseを返す'):
                expect(SampleClass(1).is_even()).to(equal(False))

    with describe('add'):
        # 副作用のある処理をテストする例
        with it('引数で指定した数を足して返す'):
            # 事前条件
            expect(self.target.number).to(equal(10))
            # 返り値テスト
            expect(self.target.add(5)).to(equal(15))
            # 事後条件
            expect(self.target.number).to(equal(15))

    with describe('http_get'):
        # 通信やファイル入出力など、IO 処理が関わるときのテスト例
        with context('200 OK'):
            with it('レスポンスボディを返す'):
                body = '{"id":1,"message":"hello"}'
                # MagicMockで処理を上書く。IO処理部分だけを行うメソッドを分離するのがミソ。
                SampleClass._http_get = MagicMock(return_value=body)
                expect(self.target.get_http_message()).to(be_a(dict))
                expect(self.target.get_http_message()['message']).to(equal('hello'))

        # patchでのテスト例
        with context('200 OK を patchで'):
            with it('レスポンスオブジェクトを返す'):
                body = '{"id":1,"message":"hello"}'
                my_response = Response()
                my_response.status_code = 200
                my_response._content = body

                # patch.object で requests.getメソッドの処理を差し替える
                with patch.object(requests, 'get', return_value=my_response):
                    expect(self.target.get_http_message()).to(be_a(dict))
                    expect(self.target.get_http_message()['message']).to(equal('hello'))
