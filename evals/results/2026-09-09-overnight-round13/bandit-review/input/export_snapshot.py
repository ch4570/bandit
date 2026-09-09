"""합성 정적 코드 발췌: 내보내기 v0.4, 2026-10-13. 실행하지 말 것.

실제 운영 코드나 실행 결과가 아니다. account는 기존 로그인 서비스가
검증한 활성 계정 정보 또는 None이며, now는 서버의 UTC 시각이다.
requested_ids는 기존 입력 검증을 통과한 중복 없는 사진 ID 목록이다.
사진의 프로젝트/분류는 이 대상 기간에 바뀌지 않지만 grants는 철회로 바뀐다.
storage는 비공개 파일 저장소다. 파일 전송은 begin_download 반환 뒤에만
시작하며, 이 경로 외에 ZIP을 직접 내려받는 공개 주소는 없다.
"""
from datetime import timedelta


def queue_export(account, requested_ids, photos, grants, now):
    if account is None or not account["active"]:
        raise PermissionError("로그인이 필요합니다")
    allowed_projects = grants.get(account["id"], set())
    for photo_id in requested_ids:
        photo = photos[photo_id]
        if photo["kind"] != "project-work" or photo["project_id"] not in allowed_projects:
            raise PermissionError("허용되지 않은 사진입니다")
    return {"requester_id": account["id"], "photo_ids": tuple(requested_ids),
            "expires_at": now + timedelta(hours=24), "ready": False}


def build_export(job, storage):
    job["artifact"] = storage.make_zip(job["photo_ids"])
    job["ready"] = True


def begin_download(job, account, now):
    if account is None or not account["active"] or account["id"] != job["requester_id"]:
        raise PermissionError("요청한 본인만 받을 수 있습니다")
    if now >= job["expires_at"]:
        raise PermissionError("만료되었습니다")
    if not job["ready"]:
        raise RuntimeError("준비 중입니다")
    return job["artifact"]
