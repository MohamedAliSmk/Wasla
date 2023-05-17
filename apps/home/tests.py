# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.test import TestCase
from .models import Merchant

class MerchantModelTestCase(TestCase):
    def setUp(self):
        self.merchant = Merchant.objects.create(
            merchant_id='123',
            merchant_name='Test Merchant',
            VPC_value=100,
            UIGmigs=50,
            VolumeCurrentMonth=500
        )

    def test_merchant_creation(self):
        """Test that a Merchant object can be created"""
        self.assertTrue(isinstance(self.merchant, Merchant))
        self.assertEqual(self.merchant.__str__(), self.merchant.merchant_name)

    def test_merchant_attributes(self):
        """Test that the Merchant object has the expected attributes"""
        self.assertEqual(self.merchant.merchant_id, '123')
        self.assertEqual(self.merchant.merchant_name, 'Test Merchant')
        self.assertEqual(self.merchant.VPC_value, 100)
        self.assertEqual(self.merchant.UIGmigs, 50)
        self.assertEqual(self.merchant.VolumeCurrentMonth, 500)

    def test_merchant_update(self):
        """Test that a Merchant object can be updated"""
        self.merchant.merchant_name = 'Updated Merchant'
        self.merchant.save()
        updated_merchant = Merchant.objects.get(pk=self.merchant.pk)
        self.assertEqual(updated_merchant.merchant_name, 'Updated Merchant')

    def test_merchant_deletion(self):
        """Test that a Merchant object can be deleted"""
        merchant_id = self.merchant.merchant_id
        self.merchant.delete()
        self.assertFalse(Merchant.objects.filter(merchant_id=merchant_id).exists())
