import { Component, OnInit } from '@angular/core';
import {FormArray, FormBuilder, Validators} from "@angular/forms";
import {FactoryConfigService} from "../../../services/factory-config/factory-config.service";

@Component({
  selector: 'app-simulation-create-view',
  templateUrl: './simulation-create-view.component.html',
  styleUrls: ['./simulation-create-view.component.scss']
})
export class SimulationCreateViewComponent implements OnInit {
  appearance: string = 'standard'

  constructor(private formBuilder: FormBuilder, private factoryConfigService: FactoryConfigService) { }

  ngOnInit(): void {
  }


  factoryConfigForm = this.formBuilder.group({
    requiredItemNames: this.formBuilder.array(
    [
      this.formBuilder.control(
        'A', [
          Validators.required,
          Validators.pattern('([\\w\\-]+)')
        ]
      )
    ]
    ),
    productCode: ['P', Validators.required],
    emptyCode: ['E', Validators.required],
    numberOfSimulationSteps: ['10', [Validators.min(1), Validators.required]],
    numberOfConveyorBeltSlots: ['3', [Validators.min(1), Validators.required]],
    numberOfWorkerPairs: ['3', [Validators.min(1), Validators.required]],
    pickupTime: ['1', [Validators.min(1), Validators.required]],
    dropTime: ['1', [Validators.min(1), Validators.required]],
    buildTime: ['4', [Validators.min(1), Validators.required]],
  })

  get requiredItemNames() {
    return this.factoryConfigForm.get('requiredItemNames') as FormArray;
  }

  addRequiredItemName() {
    this.requiredItemNames.push(this.formBuilder.control('A'))
  }

  deleteRequiredItemName(index: number) {
    this.requiredItemNames.removeAt(index)
  }

  onSubmit() {
    this.factoryConfigService.create(this.factoryConfigForm.value).subscribe();
  }

  isControlInvalid(controlName: string): boolean {
    return this.factoryConfigForm.get(controlName).invalid;
  }

  getRequiredItemNamesErrorMessage(index: number): string {
    let message = 'This field is required';
    if (this.requiredItemNames.controls[index].hasError('pattern')) {
      message = 'Only letters, numbers, - and _ are allowed.';
    }

    return message;
  }
}
