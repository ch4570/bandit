# Product journey QA design

## 요약

대상은 합성 요구 두 건에 대한 답변 품질이다. 원시 입력과 별도 의미 기준을 고정한 뒤, 평가 실행 담당자가 저장한 응답을 검토한다. 이 설계에서는 제품 스킬 실행, 테스트 러너, 브라우저, API, 빌드, 고객 접촉을 수행하지 않는다.

## 테스트 전략

개별 응답의 의미 계약을 단위 산출물 검사로 배치한다. 소프트웨어 함수 단위 테스트나 배포 환경의 E2E 실행 결과를 뜻하지 않는다. `unit`은 이 정적 산출물 검사의 최소 평가 단위라는 계약상 분류다. API·UI 수명주기 인계는 해당하지 않으므로 JSON `handoffs`는 비워 둔다. 실제 모델 호출은 저장소의 기존 독립 평가 흐름 담당자에게 맡긴다.

위험 점수는 설계자의 상대적인 영향×발생가능성 추정(각 1~3)이다. 품질 발생률 측정값이 아니다. 근거 없는 사업 판단, 현금/인력 한도 초과, 고객 약속과 과금·운영의 불일치는 영향 3×가능성 3의 P0로 둔다. 추가 관찰 계획과 정확한 문구 보존은 영향 2×가능성 2의 P1로 둔다. P0/P1은 내부 게이트이며 ISTQB의 표준 등급을 주장하지 않는다.

기법은 출처·요금·지원 가능성의 동등분할, 가격·자원·회차 한도의 경계값, 역할·수량·첫 주문 조합의 결정표, 접수→검토→결제→확정 순서의 상태전이를 적용한다. 두 고정 사례만으로 전체 조합이나 모델의 반복 신뢰도를 커버했다고 주장하지 않는다. 이 분류는 QA 번들의 `test-design-techniques.md`, `risk-coverage.md`에 정리된 [ISTQB Foundation](https://www.istqb.org/) 근거를 사용한다. Gherkin 표기는 번들의 `acceptance-criteria-gherkin.md`와 [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)에 따른다.

## 테스트 케이스

공통 전제는 원시 입력·평가 기준이 고정되고, 실행자에게 기준이 전달되지 않은 새 세션의 저장 응답이 준비된 상태다. 입력은 각 원시 사례의 합성 자료이며 제품 실행을 지시하는 단계가 아니다. 아래 기대결과의 상세 판정은 같은 폴더의 두 사례 기준에 있다.

| 케이스 ID | 요구/위험 | 전제 | 입력 | 단계 | 기대결과 | 우선순위 | 유형(기법) | 레벨 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-JOURNEY-001 | REQ-J12-1 / RISK-J12-1 | 공통 | 사례 12 연구 기록 | 저장 응답의 J12-1을 대조 | 관찰·발언·가설과 분모를 구분하고 다음 결정에 연결 | P0 | 정상·네거티브(EP: 근거 수준) | 단위 산출물 |
| TC-JOURNEY-002 | REQ-J12-2 / RISK-J12-2 | 공통 | 사례 12 역할·범위 | J12-2 대조 | 구매자/사용자와 첫 제공물을 구분하고 운영 범위 준수 | P0 | 경계·네거티브(EP/BVA) | 단위 산출물 |
| TC-JOURNEY-003 | REQ-J12-3 / RISK-J12-3 | 공통 | 사례 12 채널·요청 | J12-3 대조 | 문구·CTA·가능 채널·측정 단위·진행/중단 규칙 연결 | P0 | 정상·네거티브(결정표: 접근/신호/판단) | 단위 산출물 |
| TC-JOURNEY-004 | REQ-J12-4 / RISK-J12-4 | 공통 | 사례 12 역할·사용 기록 | J12-4 대조 | 읽음과 완료를 구분한 주 흐름·첫 사용·미인계 후 행동 명시 | P0 | 정상·엣지(상태전이) | 단위 산출물 |
| TC-JOURNEY-005 | REQ-J12-5 / RISK-J12-5 | 공통 | 사례 12 비용 | J12-5 대조·계산 확인 | 두 모델·잠정 추천·비용 포함 계산·고정비/온보딩 구분 | P0 | 경계(결정표: 과금·기간·비용) | 단위 산출물 |
| TC-JOURNEY-006 | REQ-J12-6 / RISK-J12-6 | 공통 | 사례 12 시간·현금 | J12-6 대조 | 담당·순서·의사결정과 한도 내 실행안 제시 | P0 | 경계·네거티브(BVA: 한도) | 단위 산출물 |
| TC-JOURNEY-007 | REQ-J12-7 / RISK-J12-7 | 공통 | 사례 12 불완전 기록 | J12-7 대조 | 특정 표본/지원 한계를 다음 관찰에 반영 | P1 | 엣지(EP: 불완전 근거) | 단위 산출물 |
| TC-OFFER-001 | REQ-J13-1 / RISK-J13-1 | 공통 | 사례 13 O-1/O-4·초안 | J13-1 대조 | 지리·수거 방식·반환 시점의 관련 문서 충돌 식별 | P0 | 네거티브(결정표: 지역/방식/시점) | 단위 산출물 |
| TC-OFFER-002 | REQ-J13-2 / RISK-J13-2 | 공통 | 사례 13 무료 시범 | J13-2 대조 | 만족 분모와 검사 없는 살균 주장 오류 식별 | P0 | 네거티브(EP: 근거 유무) | 단위 산출물 |
| TC-OFFER-003 | REQ-J13-3 / RISK-J13-3 | 공통 | 사례 13 O-3·가격 | J13-3 대조·계산 확인 | 첫 주문 1/2켤레 19,000/33,000과 관련 문구 교정 근거 | P0 | 경계(결정표: 수량/할인/운송비) | 단위 산출물 |
| TC-OFFER-004 | REQ-J13-4 / RISK-J13-4 | 공통 | 사례 13 24켤레 한도 | J13-4 대조 | 주문 수와 켤레 수를 구분하고 결제 전 용량 확인 요구 | P0 | 경계·네거티브(BVA: 23+1/23+2켤레) | 단위 산출물 |
| TC-OFFER-005 | REQ-J13-5 / RISK-J13-5 | 공통 | 사례 13 소재·결제 순서 | J13-5 대조 | 접수 대상/수량 확인 후 결제·성공 후 확정 순서 식별 | P0 | 네거티브(무효 상태전이) | 단위 산출물 |
| TC-OFFER-006 | REQ-J13-6 / RISK-J13-6 | 공통 | 사례 13 요청·승인 상태 | J13-6 대조 | 근거 있는 최소 수정 리뷰, 미승인 보상은 미결 유지 | P0 | 정상·네거티브(EP: 승인/초안/미결) | 단위 산출물 |
| TC-OFFER-007 | REQ-J13-7 / RISK-J13-7 | 공통 | 사례 13 정확한 초안 부분 | J13-7 대조 | 두 가지 이상 맞는 요소 보존·개선 제안과 오류 구분 | P1 | 정상(EP: 올바른 자료) | 단위 산출물 |

## 추적성 매트릭스

각 요구의 의미는 해당 `J12-n` 또는 `J13-n` 기준이고, 위험은 그 기준의 위반이다. 정확한 양방향 행과 P0 근거는 JSON에 기록했다. 이는 설계 커버리지이며 실행 통과율이 아니다.

| 요구 ID | 위험 ID | 커버 케이스 | 상태 |
| --- | --- | --- | --- |
| REQ-J12-1 | RISK-J12-1 | TC-JOURNEY-001 | 설계 커버 |
| REQ-J12-2 | RISK-J12-2 | TC-JOURNEY-002 | 설계 커버 |
| REQ-J12-3 | RISK-J12-3 | TC-JOURNEY-003 | 설계 커버 |
| REQ-J12-4 | RISK-J12-4 | TC-JOURNEY-004 | 설계 커버 |
| REQ-J12-5 | RISK-J12-5 | TC-JOURNEY-005 | 설계 커버 |
| REQ-J12-6 | RISK-J12-6 | TC-JOURNEY-006 | 설계 커버 |
| REQ-J12-7 | RISK-J12-7 | TC-JOURNEY-007 | 설계 커버 |
| REQ-J13-1 | RISK-J13-1 | TC-OFFER-001 | 설계 커버 |
| REQ-J13-2 | RISK-J13-2 | TC-OFFER-002 | 설계 커버 |
| REQ-J13-3 | RISK-J13-3 | TC-OFFER-003 | 설계 커버 |
| REQ-J13-4 | RISK-J13-4 | TC-OFFER-004 | 설계 커버 |
| REQ-J13-5 | RISK-J13-5 | TC-OFFER-005 | 설계 커버 |
| REQ-J13-6 | RISK-J13-6 | TC-OFFER-006 | 설계 커버 |
| REQ-J13-7 | RISK-J13-7 | TC-OFFER-007 | 설계 커버 |

## 인수기준

```gherkin
Feature: Saved planning outputs preserve source-grounded meaning
  Scenario: Assess a connected launch plan without disclosing the criteria to its author
    Given the frozen synthetic case 12 and its separately retained criteria
    And an independently saved response with an output hash
    When the evaluator compares the response with J12-1 through J12-7
    Then every criterion has an evidence-linked verdict
    And any incomplete P0 leaves the case failed rather than averaged away

  Scenario Outline: Assess capacity claims at the offer boundary
    Given the approved limit is 24 pairs across both complexes
    And a hypothetical session has 23 reserved pairs
    When the evaluator checks the review's treatment of a request for <pairs> pairs
    Then the stated rule supports <result> before charging

    Examples:
      | pairs | result                                    |
      | 1     | reservation in that session if eligible    |
      | 2     | another available session without charging |
```

## 실행 인계와 기계 검증

모델 실행은 이 설계의 작업 범위가 아니다. 평가 담당자는 기준을 제외한 원시 입력과 비교할 지침만 새 세션에 제공하고 원본 해시·응답·로그·실패를 보존한다. 본 설계자는 시험 실행이나 실험을 수행하지 않았다. API/UI 실행 시나리오와 외부 시드 데이터가 없으므로 실행 에이전트에 넘길 수명주기 항목은 없다.

기계 명세: `test-design.qa-plan.json`. QA 번들의 `validate-test-plan.js`로 정적 계약을 확인하며, 성공 여부와 고정 해시는 `freeze.json`에 기록한다. 정적 계약 성공은 실제 응답의 의미 평가 통과를 뜻하지 않는다.
