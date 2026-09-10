def open_link(proposal):
    proposal['status'] = 'accepted'
    return proposal


def update_amount(proposal, amount):
    proposal['amount'] = amount
    return proposal
