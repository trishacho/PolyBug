<?php

use PHPUnit\Framework\TestCase;
use YourNamespace\CategoryHelper;
use Magento\Catalog\Model\Category;

class CategoryHelperTest extends TestCase
{
    public function testIsCategoryPageReturnsFalseWhenNoCategoryId()
    {
        $categoryMock = $this->createMock(Category::class);
        $categoryMock->method('getId')->willReturn(null);

        $helperMock = $this->getMockBuilder(CategoryHelper::class)
            ->onlyMethods(['getCurrentCategory'])
            ->getMock();

        $helperMock->method('getCurrentCategory')->willReturn($categoryMock);

        $this->assertFalse($helperMock->isCategoryPage());
    }

    public function testIsCategoryPageReturnsFalseWhenDisplayModeIsContent()
    {
        $categoryMock = $this->createMock(Category::class);
        $categoryMock->method('getId')->willReturn(1);
        $categoryMock->method('getDisplayMode')->willReturn(Category::DM_PAGE);

        $helperMock = $this->getMockBuilder(CategoryHelper::class)
            ->onlyMethods(['getCurrentCategory'])
            ->getMock();

        $helperMock->method('getCurrentCategory')->willReturn($categoryMock);

        $this->assertFalse($helperMock->isCategoryPage());
    }

    public function testIsCategoryPageReturnsTrueForValidCategoryWithNonContentMode()
    {
        $categoryMock = $this->createMock(Category::class);
        $categoryMock->method('getId')->willReturn(1);
        $categoryMock->method('getDisplayMode')->willReturn('PRODUCTS');

        $helperMock = $this->getMockBuilder(CategoryHelper::class)
            ->onlyMethods(['getCurrentCategory'])
            ->getMock();

        $helperMock->method('getCurrentCategory')->willReturn($categoryMock);

        $this->assertTrue($helperMock->isCategoryPage());
    }
}
