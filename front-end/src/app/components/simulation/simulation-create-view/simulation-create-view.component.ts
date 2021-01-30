import {Component, OnInit} from '@angular/core';
import {Form, FormArray, FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import {FactoryConfigService} from '../../../services/factory-config/factory-config.service';

@Component({
  selector: 'app-simulation-create-view',
  templateUrl: './simulation-create-view.component.html',
  styleUrls: ['./simulation-create-view.component.scss']
})
export class SimulationCreateViewComponent implements OnInit {
  appearance = 'standard';

  constructor(private fb: FormBuilder, private factoryConfigService: FactoryConfigService) {
  }

  simulationForm = this.fb.group({
    name: ['', Validators.required],
    description: [''],
    factoryConfigs: this.fb.array([this.factoryConfigFormGroup]),
  });


  ngOnInit(): void {
  }

  get factoryConfigFormGroup(): FormGroup {
    return this.fb.group(
      {
        materials: this.fb.array([this.materialControl]),
        productCode: ['P', Validators.required],
        emptyCode: ['E', Validators.required],
        numberOfSimulationSteps: ['10', [Validators.min(1), Validators.required]],
        numberOfConveyorBeltSlots: ['3', [Validators.min(1), Validators.required]],
        numberOfWorkerPairs: ['3', [Validators.min(1), Validators.required]],
        pickupTime: ['1', [Validators.min(1), Validators.required]],
        dropTime: ['1', [Validators.min(1), Validators.required]],
        buildTime: ['4', [Validators.min(1), Validators.required]],
      }
    );
  }

  get materialControl() {
    return this.fb.control(
      'A', [Validators.required, Validators.pattern('([\\w\\-]+)')]
    ) as FormControl;
  }

  get factoryConfigs() {
    return this.simulationForm.get('factoryConfigs') as FormArray;
  }


  addMaterial(factoryConfig) {
    factoryConfig.get('materials').push(this.materialControl);
  }

  deleteMaterial(factoryConfig, materialIndex: number) {
    factoryConfig.get('materials').removeAt(materialIndex);
  }

  getControls(formElement, path: string) {
    return formElement.get(path)['controls'];
  }

  onSubmit() {
    this.factoryConfigService.create(this.simulationForm.value).subscribe();
  }

  isControlInvalid(formPart: FormGroup, controlName: string): boolean {
    return formPart.get(controlName).invalid;
  }

  getFactoryConfig(index: number) {
    return this.factoryConfigs.controls[index] as FormGroup;
  }

  getMaterialErrorMessage(factoryConfig, materialIndex: number): string {
    let message = 'This field is required';

    if (factoryConfig.get('materials')['controls'][materialIndex].hasError('pattern')) {
      message = 'Only letters, numbers, - and _ are allowed.';
    }

    return message;
  }
}
