# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    BaseResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy
__all__ = [
    "SubRate",
    "TaxCategory",
    "TaxCategoryAddTaxRateAction",
    "TaxCategoryChangeNameAction",
    "TaxCategoryDraft",
    "TaxCategoryPagedQueryResponse",
    "TaxCategoryReference",
    "TaxCategoryRemoveTaxRateAction",
    "TaxCategoryReplaceTaxRateAction",
    "TaxCategoryResourceIdentifier",
    "TaxCategorySetDescriptionAction",
    "TaxCategorySetKeyAction",
    "TaxCategoryUpdate",
    "TaxCategoryUpdateAction",
    "TaxRate",
    "TaxRateDraft",
]


class SubRate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.SubRateSchema`."
    #: :class:`str`
    name: str
    #: :class:`float`
    amount: float

    def __init__(self, *, name: str = None, amount: float = None) -> None:
        self.name = name
        self.amount = amount
        super().__init__()

    def __repr__(self) -> str:
        return "SubRate(name=%r, amount=%r)" % (self.name, self.amount)


class TaxCategory(BaseResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategorySchema`."
    #: :class:`str`
    id: str
    #: :class:`int`
    version: int
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: datetime.datetime
    #: :class:`datetime.datetime` `(Named` ``lastModifiedAt`` `in Commercetools)`
    last_modified_at: datetime.datetime
    #: Optional :class:`commercetools.types.LastModifiedBy` `(Named` ``lastModifiedBy`` `in Commercetools)`
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Optional :class:`commercetools.types.CreatedBy` `(Named` ``createdBy`` `in Commercetools)`
    created_by: typing.Optional["CreatedBy"]
    #: :class:`str`
    name: str
    #: Optional :class:`str`
    description: typing.Optional[str]
    #: List of :class:`commercetools.types.TaxRate`
    rates: typing.List["TaxRate"]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        id: str = None,
        version: int = None,
        created_at: datetime.datetime = None,
        last_modified_at: datetime.datetime = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        name: str = None,
        description: typing.Optional[str] = None,
        rates: typing.List["TaxRate"] = None,
        key: typing.Optional[str] = None
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.name = name
        self.description = description
        self.rates = rates
        self.key = key
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "TaxCategory(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, name=%r, description=%r, rates=%r, key=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.name,
                self.description,
                self.rates,
                self.key,
            )
        )


class TaxCategoryDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryDraftSchema`."
    #: :class:`str`
    name: str
    #: Optional :class:`str`
    description: typing.Optional[str]
    #: List of :class:`commercetools.types.TaxRateDraft`
    rates: typing.List["TaxRateDraft"]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        name: str = None,
        description: typing.Optional[str] = None,
        rates: typing.List["TaxRateDraft"] = None,
        key: typing.Optional[str] = None
    ) -> None:
        self.name = name
        self.description = description
        self.rates = rates
        self.key = key
        super().__init__()

    def __repr__(self) -> str:
        return "TaxCategoryDraft(name=%r, description=%r, rates=%r, key=%r)" % (
            self.name,
            self.description,
            self.rates,
            self.key,
        )


class TaxCategoryPagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryPagedQueryResponseSchema`."
    #: :class:`int`
    limit: int
    #: :class:`int`
    count: int
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: int
    #: List of :class:`commercetools.types.TaxCategory`
    results: typing.Sequence["TaxCategory"]

    def __init__(
        self,
        *,
        limit: int = None,
        count: int = None,
        total: typing.Optional[int] = None,
        offset: int = None,
        results: typing.Sequence["TaxCategory"] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "TaxCategoryPagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class TaxCategoryReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryReferenceSchema`."
    #: Optional :class:`commercetools.types.TaxCategory`
    obj: typing.Optional["TaxCategory"]

    def __init__(
        self,
        *,
        type_id: "ReferenceTypeId" = None,
        id: str = None,
        obj: typing.Optional["TaxCategory"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.TAX_CATEGORY, id=id)

    def __repr__(self) -> str:
        return "TaxCategoryReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class TaxCategoryResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.TAX_CATEGORY, id=id, key=key)

    def __repr__(self) -> str:
        return "TaxCategoryResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class TaxCategoryUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryUpdateSchema`."
    #: :class:`int`
    version: int
    #: :class:`list`
    actions: list

    def __init__(self, *, version: int = None, actions: list = None) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "TaxCategoryUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


class TaxCategoryUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryUpdateActionSchema`."
    #: :class:`str`
    action: str

    def __init__(self, *, action: str = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "TaxCategoryUpdateAction(action=%r)" % (self.action,)


class TaxRate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxRateSchema`."
    #: Optional :class:`str`
    id: typing.Optional[str]
    #: :class:`str`
    name: str
    #: :class:`float`
    amount: float
    #: :class:`bool` `(Named` ``includedInPrice`` `in Commercetools)`
    included_in_price: bool
    #: :class:`str`
    country: "str"
    #: Optional :class:`str`
    state: typing.Optional[str]
    #: Optional list of :class:`commercetools.types.SubRate` `(Named` ``subRates`` `in Commercetools)`
    sub_rates: typing.Optional[typing.List["SubRate"]]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        name: str = None,
        amount: float = None,
        included_in_price: bool = None,
        country: "str" = None,
        state: typing.Optional[str] = None,
        sub_rates: typing.Optional[typing.List["SubRate"]] = None
    ) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.included_in_price = included_in_price
        self.country = country
        self.state = state
        self.sub_rates = sub_rates
        super().__init__()

    def __repr__(self) -> str:
        return (
            "TaxRate(id=%r, name=%r, amount=%r, included_in_price=%r, country=%r, state=%r, sub_rates=%r)"
            % (
                self.id,
                self.name,
                self.amount,
                self.included_in_price,
                self.country,
                self.state,
                self.sub_rates,
            )
        )


class TaxRateDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxRateDraftSchema`."
    #: :class:`str`
    name: str
    #: Optional :class:`float`
    amount: typing.Optional[float]
    #: :class:`bool` `(Named` ``includedInPrice`` `in Commercetools)`
    included_in_price: bool
    #: :class:`str`
    country: "str"
    #: Optional :class:`str`
    state: typing.Optional[str]
    #: Optional list of :class:`commercetools.types.SubRate` `(Named` ``subRates`` `in Commercetools)`
    sub_rates: typing.Optional[typing.List["SubRate"]]

    def __init__(
        self,
        *,
        name: str = None,
        amount: typing.Optional[float] = None,
        included_in_price: bool = None,
        country: "str" = None,
        state: typing.Optional[str] = None,
        sub_rates: typing.Optional[typing.List["SubRate"]] = None
    ) -> None:
        self.name = name
        self.amount = amount
        self.included_in_price = included_in_price
        self.country = country
        self.state = state
        self.sub_rates = sub_rates
        super().__init__()

    def __repr__(self) -> str:
        return (
            "TaxRateDraft(name=%r, amount=%r, included_in_price=%r, country=%r, state=%r, sub_rates=%r)"
            % (
                self.name,
                self.amount,
                self.included_in_price,
                self.country,
                self.state,
                self.sub_rates,
            )
        )


class TaxCategoryAddTaxRateAction(TaxCategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryAddTaxRateActionSchema`."
    #: :class:`commercetools.types.TaxRateDraft` `(Named` ``taxRate`` `in Commercetools)`
    tax_rate: "TaxRateDraft"

    def __init__(self, *, action: str = None, tax_rate: "TaxRateDraft" = None) -> None:
        self.tax_rate = tax_rate
        super().__init__(action="addTaxRate")

    def __repr__(self) -> str:
        return "TaxCategoryAddTaxRateAction(action=%r, tax_rate=%r)" % (
            self.action,
            self.tax_rate,
        )


class TaxCategoryChangeNameAction(TaxCategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryChangeNameActionSchema`."
    #: :class:`str`
    name: str

    def __init__(self, *, action: str = None, name: str = None) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "TaxCategoryChangeNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class TaxCategoryRemoveTaxRateAction(TaxCategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryRemoveTaxRateActionSchema`."
    #: :class:`str` `(Named` ``taxRateId`` `in Commercetools)`
    tax_rate_id: str

    def __init__(self, *, action: str = None, tax_rate_id: str = None) -> None:
        self.tax_rate_id = tax_rate_id
        super().__init__(action="removeTaxRate")

    def __repr__(self) -> str:
        return "TaxCategoryRemoveTaxRateAction(action=%r, tax_rate_id=%r)" % (
            self.action,
            self.tax_rate_id,
        )


class TaxCategoryReplaceTaxRateAction(TaxCategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategoryReplaceTaxRateActionSchema`."
    #: :class:`str` `(Named` ``taxRateId`` `in Commercetools)`
    tax_rate_id: str
    #: :class:`commercetools.types.TaxRateDraft` `(Named` ``taxRate`` `in Commercetools)`
    tax_rate: "TaxRateDraft"

    def __init__(
        self,
        *,
        action: str = None,
        tax_rate_id: str = None,
        tax_rate: "TaxRateDraft" = None
    ) -> None:
        self.tax_rate_id = tax_rate_id
        self.tax_rate = tax_rate
        super().__init__(action="replaceTaxRate")

    def __repr__(self) -> str:
        return (
            "TaxCategoryReplaceTaxRateAction(action=%r, tax_rate_id=%r, tax_rate=%r)"
            % (self.action, self.tax_rate_id, self.tax_rate)
        )


class TaxCategorySetDescriptionAction(TaxCategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategorySetDescriptionActionSchema`."
    #: Optional :class:`str`
    description: typing.Optional[str]

    def __init__(
        self, *, action: str = None, description: typing.Optional[str] = None
    ) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "TaxCategorySetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class TaxCategorySetKeyAction(TaxCategoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TaxCategorySetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(self, *, action: str = None, key: typing.Optional[str] = None) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "TaxCategorySetKeyAction(action=%r, key=%r)" % (self.action, self.key)
