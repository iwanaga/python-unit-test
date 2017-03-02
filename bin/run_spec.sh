#!/bin/bash

# 計測メタデータを削除
if [ -d coverage_report ]; then
  rm coverage_report/*
fi
find ./* -name '*.py,cover' -exec rm {} \;

# テスト実行
mamba --enable-coverage spec/*

# レポート
coverage report
coverage html -d coverage_report

echo ""
echo "カバーできていない箇所を探したいとき:"
echo "open coverage_report/index.html"
